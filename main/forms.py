# -*- coding: utf-8 -*-
from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=64, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'name',
        'placeholder': 'Ваше имя'
    }))
    email = forms.CharField(max_length=64, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'email',
        'placeholder': 'Ваш email'
    }))

    class Meta:
        model = Client
        exclude = [""]