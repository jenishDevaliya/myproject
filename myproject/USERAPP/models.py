from django.db import models

class UsrModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField(default=0)
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name
