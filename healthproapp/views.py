from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HealthPro

@login_required
def healthpro_dashboard(request):
    if not hasattr(request.user, 'healthpro'):
        return redirect('login_view')
    return render(request, 'healthpro/healthpro_dashboard.html')