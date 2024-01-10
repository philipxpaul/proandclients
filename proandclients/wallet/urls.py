from django.urls import path
from . import views

urlpatterns = [
    path('deposit_to_wallet/', views.deposit_to_wallet, name='deposit_to_wallet'),
]

