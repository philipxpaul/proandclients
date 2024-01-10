from django.shortcuts import render, redirect
from consultant.models import Consultant
from twilio.rest import Client
from .models import OTP, CustomUser  # Assume User is your custom user model
from django.conf import settings
import random

# Create your views here.
def home(request):
    return render(request,'home.html')

def consultant(request):
    consultants = Consultant.objects.all()  # Assuming you have a Consultant model with objects to display
    return render(request, 'consultant.html', {'consultants': consultants})

def signup(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        # Here, create a new user or update the existing user
        # Redirect to login or directly to OTP verification
        return redirect('send_otp')
    return render(request, 'signup.html')

def send_otp(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        otp = str(random.randint(100000, 999999))
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f"Your OTP is {otp}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        OTP.objects.create(user=CustomUser.objects.get(phone_number=phone_number), otp=otp)  # Create OTP record
        return redirect('verify_otp')
    return render(request, 'login.html')

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        user_otp = OTP.objects.get(user=request.user)  # Get the user's last OTP
        if user_otp.otp == entered_otp and user_otp.is_valid():
            # Log the user in and redirect to home or dashboard
            login(request, user_otp.user)
            return redirect('home')
        else:
            # Handle invalid or expired OTP
            pass
    return render(request, 'verify_otp.html')

