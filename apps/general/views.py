from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..utils.models import IsAdminUser
from .models import PaymentMethod, University
from .serializers import PaymentMethodSerializer, UniversitySerializer


class PaymentMethodListCreateView(ListCreateAPIView):
    """ This class is used to list and create ApiViews payment methods."""
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]


class PaymentMethodDetailView(RetrieveUpdateDestroyAPIView):
    """ This class is used to retrieve,update and delete ApiViews payment methods."""
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UniversityListCreateView(ListCreateAPIView):
    """ This class is used to list and create ApiViews universities."""
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny]

class UniversityDetailView(RetrieveUpdateDestroyAPIView):
    """ This class is used to retrieve,update and delete ApiViews universities."""
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]



