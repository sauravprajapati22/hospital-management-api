from django.db import models
from django.conf import settings

# Create your models here.

class PatientProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_profile"
    )
    age = models.IntegerField(blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    medical_history = models.TextField(blank=True , null=True)

    def __str__(self):
        return self.user.username