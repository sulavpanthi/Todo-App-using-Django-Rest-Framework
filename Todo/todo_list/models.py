from django.db import models

# Create your models here.
class TodoList(models.Model):
    list_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    