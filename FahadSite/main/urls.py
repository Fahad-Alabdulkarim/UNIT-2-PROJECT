from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_us, name='contact_us'),
    path('contact/messages/', views.contact_messages, name='contact_messages'),
]
