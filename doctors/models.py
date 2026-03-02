from django.db import models
from django.conf import settings

# Create your models here.

class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="doctor_profile")
    specialization  = models.CharField(max_length=100, blank=True, null=True)
    experience = models.IntegerField(help_text="Experience in years", blank=True, null=True)
    hospital_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"