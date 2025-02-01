from django.urls import path
from .views import StudentSponsorListCreateView, StudentSponsorDetailView

urlpatterns = [
    path('sponsors/', StudentSponsorListCreateView.as_view(), name='studentsponsor-list-create'),
    path('sponsors/<int:pk>/', StudentSponsorDetailView.as_view(), name='studentsponsor-detail'),
]
