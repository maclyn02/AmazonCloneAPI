from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
