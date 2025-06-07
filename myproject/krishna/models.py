# krishna/models.py
import numbers
from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=15, blank=True, null=True)  # Add a number field
    email = models.EmailField(blank=True, null=True)  # Add an email field

    def __str__(self):
        return self.name
