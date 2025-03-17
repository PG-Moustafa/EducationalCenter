from django.urls import path
from .views import generate_certificate_pdf

urlpatterns = [
    path('certificate/<int:user_id>/', generate_certificate_pdf, name='generate_certificate_pdf'),
]