from django.urls import path
from . import views

app_name = 'childapp'

urlpatterns = [
    path('add/', views.add_child, name='add_child'),
    path('childapp/child_dashboard/', views.child_dashboard, name='child_dashboard'),
]