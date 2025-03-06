from django.shortcuts import render,redirect
from django.http import HttpResponse

from trainerapp.models import Trainer
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def guardian_dashboard(request):
    return render(request,"guardian/guardian_dashboard.html")
def child_dashboard(request):
    return render(request,"childapp/child_dashboard.html")


    


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            login(request, user)

            if user.is_superuser:
                return redirect("/admin/")
            elif hasattr(user, 'trainer'):
                return redirect('trainer_dashboard')
            elif hasattr(user, 'guardian'):
                return redirect('guardian_dashboard')
            elif hasattr(user, 'healthpro'):
                return redirect('healthpro_dashboard')
            elif hasattr(user, 'child'):
                return redirect('child_dashboard')
            else:
                messages.error(request, "User type not found")
                return render(request, "login_view.html")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login_view.html")
    
    return render(request, "login_view.html")