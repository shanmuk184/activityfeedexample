from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from actstream import registry

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)

class Supervisor(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE, related_name="supervisor")
    task = models.ManyToManyField(Task,related_name='tasks')

# registry.register(Task)
# registry.register(Supervisor)