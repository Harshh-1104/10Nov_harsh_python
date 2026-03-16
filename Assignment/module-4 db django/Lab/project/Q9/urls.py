from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='q9_home'),
    path('about/', views.about, name='q9_about'),
    path('contact/', views.contact, name='q9_contact'),
    path('services/', views.services, name='q9_services'),
]