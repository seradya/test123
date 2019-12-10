# -*- coding: utf-8 -*-
from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from django.views.generic import CreateView
from .forms import CustomUserForm

app_name = 'auth123'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth123/login.html'), name="login"),
    path('logout/', logout_then_login, name='logout'),
    path('register/', CreateView.as_view(
        template_name='auth123/register.html',
        form_class=CustomUserForm,
        success_url='/'),
    name='register'),
]