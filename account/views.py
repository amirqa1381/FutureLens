from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, LoginForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.contrib.auth import logout
from django.contrib import messages

class UserRegisterView(FormView):
    """
    this class is for handling the registration of the user when it want to register in to the app
    Args:
        FormView (_type_): _description_
    """
    form_class = UserRegistrationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy("index")
    
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "You have been successfully registered")
        return super().form_valid(form)
    


class UserLoginView(LoginView):
    """
    this view is for login the user and it's for authentication and if user has not been authenticated 
    should go to this page and login in the site
    Args:
        LoginView (_type_): it's inherted from the contrib.auth
    """
    authentication_form = LoginForm
    template_name = "account/login.html"
    
    def form_valid(self, form):
        messages.success(self.request, "You have been successfully logged in")
        return super().form_valid(form)
    
    
    def get_success_url(self):
        return reverse_lazy("index")
    
    

def logout_view(request: HttpRequest):
    """
    this is the logout view and if user want to logout from the app can send the request to this view 
    Args:
        request (HttpRequest): _description_
    """
    logout(request)
    messages.success(request, "Logout successfully....")
    return redirect("index")