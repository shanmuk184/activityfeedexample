from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from actstream import registry
from django.db.models.signals import post_save
from django.dispatch import receiver
from actstream import action
from django.utils.translation import gettext_lazy as _
class Business(models.Model):
    name = models.CharField(max_length=64)

class Employee(models.Model):
    class EmployeeRoles(models.TextChoices):
        Owner = 1, _('Owner')
        Employee = 2, _('Employee')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    role = models.CharField(choices=EmployeeRoles.choices, max_length=64) 

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

class Job(models.Model):
    class JobStates(models.TextChoices):
        Opened = 1, _('Opened')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    state = models.CharField(choices=JobStates.choices, max_length=64)
    def __str__(self):
        return self.business.name


class Application(models.Model):
    class ApplicationState(models.TextChoices):
        Applied = 1, _('Applied')
        Shortlisted = 2, _('Shortlisted') 
        Rejected = 3, _('Rejected')
        Selected = 4, _('Selected')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete = models.CASCADE)
    state = models.CharField(choices=ApplicationState.choices, max_length=64)

@receiver(post_save, sender=Application)
def applicationUpdate(sender, instance, created, raw, update_fields, **kwargs):
    print(type(instance.user))
    print(type(instance.job))
    print(update_fields)
    action.send(instance.user, verb='Job Applied', action_object=instance.job, target=instance.user.user_city.all()[0].city)

class City(models.Model):
    name = models.CharField(max_length=64)

class UserCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_city')

