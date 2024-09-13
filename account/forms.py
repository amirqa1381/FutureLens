from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    """
    this class is for a time that we want to register a user in the database and app
    Args:
        UserCreationForm (_type_): _description_
    """

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Password",
        required=True,
        help_text="",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Cofirm password",
        required=True,
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
        }


class LoginForm(AuthenticationForm):
    """
    this class is form for login the user in the site
    Args:
        AuthenticationForm (_type_): _description_
    """

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
        label="Username",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True,
        label="Password",
    )

    class Meta:
        model = User
        fields = ["username", "password"]
