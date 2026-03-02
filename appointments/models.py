from django.db import models
from django.conf import settings

# Create your models here.
class Appointment(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="doctor_appointment")
    patient = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="patient_appointment")
    date = models.DateField(blank=True,null=True)
    time = models.TimeField(blank=True,null=True)
    reason = models.TextField(blank=True,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} -> {self.doctor.username}"
    