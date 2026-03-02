from rest_framework import serializers
from .models import DoctorProfile

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'
        read_only_fields = ['user']


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['specialization', 'experience', 'hospital_name']