from django.contrib import admin

# Register your models here.
from .models import Task, Supervisor

admin.site.register(Task)
admin.site.register(Supervisor)