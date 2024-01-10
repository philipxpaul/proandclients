from django.urls import path
from . import views 

urlpatterns = [
    path('home/', views.home, name='home'),
    path('consultant/', views.consultant, name='consultant'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.send_otp, name='send_otp'),
    path('verify/', views.verify_otp, name='verify_otp'),
]

