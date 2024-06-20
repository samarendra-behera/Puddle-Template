from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('new/', views.newItem, name='new_item'),
    path('<int:pk>/', views.detail, name='detail'),
]