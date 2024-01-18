from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

# update model

# class EventType(models.Model):
#     pass

# class Subscription(models.Model):
#     event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

# class User(AbstractUser):
#     subscription = models.ManyToManyField(Subscription)
#     org = models.CharField(max_length=255)
#     position = models.CharField(max_length=255)
#     preferences = models.CharField(max_length=255)