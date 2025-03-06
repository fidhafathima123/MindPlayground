
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import ChildRegistrationForm
from .models import Child

@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            child = form.save(commit=False)
            child.guardian = request.user
            child.save()
            messages.success(request, "Registration successful!")
            return redirect("child_dashboard")
            
        else:
            print("Invalid")
            print(form.errors)  
            messages.error(request, "Please correct the errors below.")
    else:
        form = ChildRegistrationForm()
    return render(request, 'childapp/add_child.html', {'form': form})

@login_required
def child_dashboard(request):
    
    return render(request,"childapp/child_dashboard.html")
