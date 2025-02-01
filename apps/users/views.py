from .models import CustomUser, UserModel
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class UserListCreateAPIView(ListCreateAPIView):
    """ This class is used to list and create APIview for user"""
    queryset = CustomUser.objects.filter(role__in=[UserModel.UserRole.STUDENT, UserModel.UserRole.SPONSOR])
    serializer_class = CustomUserSerializer

    filterset_fields = ['role','university']
    search_fields = ['phone_number', 'first_name', 'last_name']
    ordering_fields = ['pk', 'balance', 'date_joined', 'last_login']


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """ This class is used to retrieve and update or delete a user"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]




