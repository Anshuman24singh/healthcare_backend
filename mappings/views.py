
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

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


class PatientDoctorsOrDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        patient = get_object_or_404(
            Patient,
            pk=pk,
            created_by=request.user,
        )
        doctors = Doctor.objects.filter(
            patient_mappings__patient=patient
        ).order_by("id").distinct()

        return Response(DoctorSerializer(doctors, many=True).data)

    def delete(self, request, pk):
        mapping = get_object_or_404(
            PatientDoctorMapping.objects.filter(
                patient__created_by=request.user
            ),
            pk=pk,
        )
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
