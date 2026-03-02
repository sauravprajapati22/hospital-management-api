from django.urls import path
from .views import DoctorProfileView,DoctorListView,DoctorProfileUpdateView


urlpatterns = [
    path("profile/", DoctorProfileView.as_view()),
    path('list/',DoctorListView.as_view()),
    path('profile/', DoctorProfileUpdateView.as_view(), name='doctor-profile'),
]