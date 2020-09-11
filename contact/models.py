from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Logo(models.Model):
    image = models.ImageField(upload_to='media/logo')

class CreateUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.user.username

class TypeTask(models.Model):
    type_task = models.CharField(max_length=50)
    def __str__(self):
        return self.type_task

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(TypeTask, on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True)
    task = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    done = models.BooleanField(default=False)


class PersonalInfo(models.Model):
    image = models.ImageField(upload_to='media/personal', null=True, blank=True)
    number_code = models.CharField(max_length=2)
    number = models.CharField(max_length=7)
    number_icon = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    mail_icon = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    telegram_icon = models.CharField(max_length=50)