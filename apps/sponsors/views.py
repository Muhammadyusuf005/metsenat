from .models import StudentSponsor
from rest_framework import generics
from ..utils.models import IsAdminUser
from .serializers import StudentSponsorSerializer
from rest_framework.permissions import IsAuthenticated


class StudentSponsorListCreateView(generics.ListCreateAPIView):
    """ This class is used to list and create APIView for sponsors"""
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    filterset_fields = {
        'amount': ['lt', 'gt'],
    }
    search_fields = ['phone_number', 'first_name', 'last_name']
    ordering_fields = ['pk', 'amount', 'date_joined', 'last_login']



class StudentSponsorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ This class is used to retrieve and update and delete and APIView for sponsors"""
    queryset = StudentSponsor.objects.all()
    serializer_class = StudentSponsorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
