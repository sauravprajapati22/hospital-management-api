from django.urls import path
from .views import (AppointmentCreateView,AppointmentListView,PatientAppointmentListView,PatientAppointmentDetailView)

urlpatterns = [
    # Patient creates appointment
    path('', AppointmentCreateView.as_view(), name='appointment-create'),

    # Patient lists own appointments
    path('me/', PatientAppointmentListView.as_view(), name='patient-appointments'),

    # Patient retrieves/updates/deletes single appointment
    path('me/<int:pk>/', PatientAppointmentDetailView.as_view(), name='patient-appointment-detail'),

    # Doctor lists appointments
    path('doctor/', AppointmentListView.as_view(), name='doctor-appointments'),
]