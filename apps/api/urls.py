from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentGenerationView


urlpatterns = [
    path('generate/', DocumentGenerationView.as_view(), name='generate-document'),
    # Otras URLs de tu aplicación...
]
