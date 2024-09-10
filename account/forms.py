from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    """
    this class is for a time that we want to register a user in the database and app
    Args:
        UserCreationForm (_type_): _description_
    """

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Password", required=True, help_text=""
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Cofirm password", required= True
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    
