"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import todo.views as todo_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todo_views.ToDoListView.as_view(), name = "todo-list"),
    path('task/<int:pk>/',todo_views.ToDoDetailView.as_view(), name = "todo-detail"),
    path('create/',todo_views.ToDoCreateView.as_view(), name = "todo-create"),
    path('task/<int:pk>/update/',todo_views.ToDoUpdateView.as_view(), name = "todo-update"),
    path('task/<int:pk>/delete/',todo_views.ToDoDeleteView.as_view(), name = "todo-delete"),
    path('register/',todo_views.register, name = "register"),
    path('login/',auth_views.LoginView.as_view(template_name = 'todo/login.html'), name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'todo/logout.html'),name= 'logout'),
]
