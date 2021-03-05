from django.db import models
from django.urls import reverse

class ToDo(models.Model):
	content = models.TextField()

	def get_absolute_url(self):
		return reverse("todo-detail",kwargs = {"pk":self.pk})
