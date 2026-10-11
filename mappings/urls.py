
from django.urls import path

from .views import (
    MappingListCreateView,
    MappingDeleteView,
    PatientDoctorsView,
)

urlpatterns = [
    path("", MappingListCreateView.as_view(), name="mapping-list-create"),
    path(
        "patient/<int:patient_id>/",
        PatientDoctorsView.as_view(),
        name="patient-doctors",
    ),
    path("<int:pk>/", MappingDeleteView.as_view(), name="mapping-delete"),
]
