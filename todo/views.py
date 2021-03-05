from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ToDo
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class ToDoListView(ListView):
	model = ToDo

class ToDoDetailView(DetailView):
	model = ToDo

class ToDoCreateView(CreateView):
	model = ToDo
	fields = ["content"]

class ToDoUpdateView(UpdateView):
	model = ToDo
	fields = ["content"]
	success_url = "/"

class ToDoDeleteView(DeleteView):
	model = ToDo
	success_url = "/"

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your account has been created!")
			return redirect("/")
	else:
		form = UserCreationForm()
	context = {"form": form}
	return render(request, "todo/register.html", context)
