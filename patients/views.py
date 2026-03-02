from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PatientProfile
from .serializers import PatientSerializer

# Create your views here.

class PatientProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.patient_profile
