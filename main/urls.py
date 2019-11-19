# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('feedback', views.feedback, name="feedback"),
    path('services', views.services, name='services')
]
