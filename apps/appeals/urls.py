from django.urls import path
from .views import AppealListCreateView, AppealDetailView

urlpatterns = [
    path('appeals/', AppealListCreateView.as_view(), name='appeal-list-create'),
    path('appeals/<int:pk>/', AppealDetailView.as_view(), name='appeal-detail'),
]
