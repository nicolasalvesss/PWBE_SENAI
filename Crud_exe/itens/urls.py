from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_read, name='item_read'),
    path('create/', views.item_create, name= 'item_create'),
    path('giovana_minha_princesa/ <int:pk>', views.item_update, name='item_update'),
    path('adrian_meu_brodi/<int:pk>/', views.item_delete, name='item_delete')
]
