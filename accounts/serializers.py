from rest_framework import serializers
from django.contrib.auth import get_user_model
from doctors.models import DoctorProfile
from patients.models import PatientProfile

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        role = validated_data.get('role')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role
        )

        # 🔥 Auto create profile based on role
        if role == 'doctor':
            DoctorProfile.objects.create(user=user)
        elif role == 'patient':
            PatientProfile.objects.create(user=user)

        return user