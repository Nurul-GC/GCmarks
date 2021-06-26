from django.urls import path
from django.contrib.auth import views as vw
from accounts import views


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', vw.LoginView.as_view(), name='login'),
    path('logout/', vw.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
