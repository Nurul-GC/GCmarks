from django.urls import path
from contas import views


app_name = 'contas'
urlpatterns = [
    path('', views.inicio, name='inicio'),
]
