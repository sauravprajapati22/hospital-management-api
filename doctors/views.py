from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import DoctorProfile
from .serializers import DoctorSerializer,DoctorProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class DoctorProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.doctor_profile
    
class DoctorListView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]

    filterset_fields = ["specialization" , 'experience']
    search_fields =  ["hospital_name"]
    ordering_fields = ["expirence"]

class DoctorProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.doctor_profile