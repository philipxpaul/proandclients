from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.register_consultant, name='registration'),
    path('registration/success/', views.registration_success, name='registration_success'),  # Add this line
]

