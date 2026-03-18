from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('api/items/', views.api_item_list, name='api_item_list'),
    path('api/items/create/', views.api_item_create, name='api_item_create'),
    path('api/items/<int:item_id>/update/', views.api_item_update, name='api_item_update'),
    path('api/items/<int:item_id>/delete/', views.api_item_delete, name='api_item_delete'),
]