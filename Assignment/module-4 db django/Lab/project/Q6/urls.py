from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='q6_home'),
    path('create/', views.doctor_create, name='q6_create'),
]