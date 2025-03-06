
from django.shortcuts import render, redirect
from django.contrib.auth import login


# views.py (trainerapp/views.py)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trainer

@login_required
def trainer_dashboard(request):
    if not hasattr(request.user, 'trainer'):
        return redirect('login_view')
    return render(request, 'trainer/trainer_dashboard.html')