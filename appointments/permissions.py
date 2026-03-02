from rest_framework.permissions import BasePermission
from rest_framework import permissions
from datetime import date


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'patient'

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "doctor"
    
class IsFutureAppointment(permissions.BasePermission):
    """
    Allows modification only if the appointment is in the future.
    """

    def has_object_permission(self, request, view, obj):
        return obj.date >= date.today()