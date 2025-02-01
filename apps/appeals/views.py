from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import Appeal
from ..users.models import UserModel
from .serializers import AppealSerializer


class AppealListCreateView(ListCreateAPIView):
    """ This class is used to list and Create ApiView"""

    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != UserModel.UserRole.SPONSOR :
            raise PermissionDenied("You must be an sponsor to create an appeal.")
        serializer.save()


class AppealDetailView(RetrieveUpdateDestroyAPIView):
    """ This class is used to retrieve and Update and delete ApiView"""

    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [IsAuthenticated]




