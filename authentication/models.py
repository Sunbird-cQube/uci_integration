from django.db import models
from django.contrib.auth.models import AbstractUser

class Subscription(models.Model):
    """
    Represents Subscription in the system.

    Attributes:
        name (CharField): The name of the subscription.
        org (CharField): The organization the subscription belongs to.
    """
    name = models.CharField(max_length=255)
    org = models.CharField(max_length=255)

class Alert(models.Model):
    """
    Represents a user in the system.

    Attributes:
        subscription (ForeignKey): The user's subscriptions.
        message (TextField): The message of the alert.
        date (DateField): The date of the alert.
        users (ManyToManyField): The users who received the alert.
    """
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField()
    users = models.ManyToManyField('User')

class User(AbstractUser):
    """
    Represents a user in the system.

    Attributes:
        subscription (ManyToManyField): The user's subscriptions.
        # org (CharField): The organization the user belongs to.
        type (CharField): The type of user (admin or user).
        # position (CharField): The user's position in the organization.
        preferences (CharField): The user's preferences.
    """
    subscription = models.ManyToManyField(Subscription)
    # org = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=[('admin', 'Admin'), ('user', 'User')], default='user')
    # position = models.CharField(max_length=255)
    preferences = models.CharField(max_length=255)