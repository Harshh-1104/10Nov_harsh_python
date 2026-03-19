from django.urls import path
from . import views

urlpatterns = [
    path('q3/', views.register, name='register'),
]
