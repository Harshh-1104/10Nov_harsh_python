from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_crud_list'),
    path('add/', views.add_edit_doctor, name='doctor_crud_add'),
    path('edit/<int:pk>/', views.add_edit_doctor, name='doctor_crud_edit'),
    path('delete/<int:pk>/', views.delete_doctor, name='doctor_crud_delete'),
]
