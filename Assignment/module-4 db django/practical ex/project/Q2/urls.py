from django.urls import path
from . import views

urlpatterns = [
    path('q2/', views.doctor_profile, name='doctor_profile'),
]
