from django.urls import path
from . import views

urlpatterns = [
    
    
    path('guardian/guardian_dashboard/', views.guardian_dashboard, name='guardian_dashboard'),
    path('registration/', views.registration, name='registration'),
] 