from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='q11_home'),
    path('add/', views.book_add, name='q11_add'),
]