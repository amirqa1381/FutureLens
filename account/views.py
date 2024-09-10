from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.views.generic import FormView



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
        return super().form_valid(form)
    
    

