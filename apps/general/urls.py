from django.urls import path
from .views import UniversityListCreateView, UniversityDetailView
from .views import PaymentMethodListCreateView, PaymentMethodDetailView


urlpatterns = [
    path('universities/', UniversityListCreateView.as_view(), name='university-list-create'),
    path('universities/<uuid:pk>/', UniversityDetailView.as_view(), name='university-detail'),
    path('payment-methods/', PaymentMethodListCreateView.as_view(), name='paymentmethod-list-create'),
    path('payment-methods/<int:pk>/', PaymentMethodDetailView.as_view(), name='paymentmethod-detail'),
]
