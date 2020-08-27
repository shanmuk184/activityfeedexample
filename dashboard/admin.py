from django.contrib import admin

# Register your models here.
from .models import Job, Business, Application, City, UserCity, Employee

admin.site.register(Job)
admin.site.register(Business)
admin.site.register(Application)
admin.site.register(UserCity)
admin.site.register(City)
admin.site.register(Employee)
 