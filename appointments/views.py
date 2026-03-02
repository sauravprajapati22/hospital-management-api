from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticated
from .models import Appointment
from .serializers import AppointmentSerializer
from .permissions import IsPatient, IsDoctor, IsFutureAppointment 

class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated,IsPatient]

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)
    
class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated,IsDoctor]

    def get_queryset(self):
        return Appointment.objects.filter(doctor = self.request.user)

class PatientAppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes =[permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(patient = user).order_by('-date')
    
class PatientAppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or cancel a single appointment.
    Only the patient who owns it can modify.
    Only future appointments can be updated/deleted.
    """
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsPatient, IsFutureAppointment]

    def get_queryset(self):
        # Ensure patient can only access their own appointments
        return Appointment.objects.filter(patient=self.request.user)    