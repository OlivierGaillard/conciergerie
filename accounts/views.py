from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import reverse



class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/user_registration.html'
    
    def get_success_url(self):
        return reverse('home')



