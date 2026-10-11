
from django.urls import path
from .views import MappingListCreateView, PatientDoctorsOrDeleteView

urlpatterns = [
    path("", MappingListCreateView.as_view(), name="mapping-list-create"),
    path("<int:pk>/", PatientDoctorsOrDeleteView.as_view(), name="patient-doctors-or-delete"),
]
