from django.urls import path

from .views import MasterAPIView, MasterRetrieveAPIView, ServiceAPIView, ServiceRetrieveAPIView, RequestAPIView, RequestRetrieveAPIView

urlpatterns = [
    path('master/', MasterAPIView.as_view()),
    path('master/<int:pk>/', MasterRetrieveAPIView.as_view()),
    # Product
    path('service/', ServiceAPIView.as_view()),
    path('service/<int:pk>/', ServiceRetrieveAPIView.as_view()),
    # Images
    path('request/', RequestAPIView.as_view()),
    path('request/<int:pk>/', RequestRetrieveAPIView.as_view()),
]