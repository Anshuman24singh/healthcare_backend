from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from patients.models import Patient
from doctors.models import Doctor
from .models import PatientDoctorMapping
from .serializers import MappingSerializer
from doctors.serializers import DoctorSerializer


class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        ).select_related("patient", "doctor").order_by("id")

    def perform_create(self, serializer):
        serializer.save(assigned_by=self.request.user)


class MappingDeleteView(generics.DestroyAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )


class PatientDoctorsView(generics.ListAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient = get_object_or_404(
            Patient,
            pk=self.kwargs["patient_id"],
            created_by=self.request.user,
        )

        return Doctor.objects.filter(
            patient_mappings__patient=patient
        ).order_by("id").distinct()
