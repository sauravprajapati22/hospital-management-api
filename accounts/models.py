from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('doctor' , 'Doctor'),
        ('patient' , 'Patient'),
    )

    role = models.CharField(max_length=35,choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
    