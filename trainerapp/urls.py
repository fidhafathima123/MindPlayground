from django.urls import path
from .import views

urlpatterns = [

    path('dashboard/', views.trainer_dashboard, name='trainer_dashboard'),
]
