from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('<str:model_name>/', views.dashboard, name='dashboard_model'),
]