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
    path('edit/', views.edit, name='edit'),
    path('password_change/', vw.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', vw.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
