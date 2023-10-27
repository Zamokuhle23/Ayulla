
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.viewsets import DoctorViewSet,PatientViewSet,AppointmentViewSet

router = routers.DefaultRouter()
router.register('doctors',DoctorViewSet)
router.register('patients',PatientViewSet)
router.register('patients',PatientViewSet)
router.register('doctors',DoctorViewSet)
router.register('appointments',AppointmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    
    
]
