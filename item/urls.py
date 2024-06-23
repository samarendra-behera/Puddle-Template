from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('new/', views.newItem, name='new_item'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete_item, name='delete'),
    path('<int:pk>/edit/', views.edit_item, name='edit'),
]