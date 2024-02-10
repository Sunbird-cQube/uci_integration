from django.db import models
from django.contrib.auth.models import AbstractUser

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    org = models.CharField(max_length=255)

class Alert(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField()
    users = models.ManyToManyField('User')

class User(AbstractUser):
    subscription = models.ManyToManyField(Subscription)
    org = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=[('admin', 'Admin'), ('user', 'User')], default='user')
    position = models.CharField(max_length=255)
    preferences = models.CharField(max_length=255)