from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_us, name='contact_us'),
    path('contact/messages/', views.contact_messages, name='contact_messages'),
    path('about/', views.about, name='about'),
    path('contact/<int:id>/', views.contacts_view, name='contacts_detail'),
    path('contact/<int:id>/delete/', views.contacts_delete, name='contacts_delete'),
]
