from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='q12_home'),
    path('create/', views.product_create, name='q12_create'),
    path('<int:pk>/update/', views.product_update, name='q12_update'),
    path('<int:pk>/delete/', views.product_delete, name='q12_delete'),
]