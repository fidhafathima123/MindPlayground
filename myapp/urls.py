from django.urls import path,include
from . import views

urlpatterns = [
    
    path("", views.index),
    path('login_view/', views.login_view, name='login_view'),
    path('guardian/guardian_dashboard/', views.guardian_dashboard, name='guardian_dashboard'),
    path('childapp/child_dashboard/', views.child_dashboard, name='child_dashboard'),
    
]   
