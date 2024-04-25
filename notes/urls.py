from django.urls import path

from . import views

urlpatterns = [
    path('api/stock/', views.stock_list, name='stock_list'),
]