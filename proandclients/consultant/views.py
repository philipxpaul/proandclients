from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Consultant
from .forms import ConsultantForm

def register_consultant(request):
    if request.method == 'POST':
        form = ConsultantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Make sure you have a URL pattern named 'registration_success'
        else:
            # If form is not valid, re-render the registration page with the form containing errors
            return render(request, 'registration.html', {'form': form})
    else:
        form = ConsultantForm()
    return render(request, 'registration.html', {'form': form})


def registration_success(request):
    return HttpResponse("You have registered successfully!")


