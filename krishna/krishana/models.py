# krishana/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class KrishanaUser(AbstractUser):
    # Add any additional fields you want for your custom user model
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username
