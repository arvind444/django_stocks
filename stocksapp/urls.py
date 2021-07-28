from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_stocks/', views.add_stocks, name='add_stocks'),
    path('delete/<stocks_id>', views.delete, name='delete'),
    path('delete_stocks', views.delete_stocks, name='delete_stocks' ),
]
