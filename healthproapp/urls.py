from django.urls import path
from .import views

urlpatterns = [

    path('healthpro_dashboard/', views.healthpro_dashboard, name='healthpro_dashboard'),
]