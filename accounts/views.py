from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import reverse


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        labels = {
            'username' : 'Utilisateur /-trice',
        }

        help_texts = {

            'username' : 'Requis. 150 characters ou moins. Lettres, chiffres et @/./+/-/_  uniquement.'
        }


    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['password1'].label = "Mot de passe"
        help_txt_passwd1 = """<ul>
                <li>Votre mot de passse doit contenir au moins 6 caractères.</li>
                <li>Votre mot de passse ne doit pas contenir que des chiffres.</li>
                </ul>"""
        self.fields['password1'].help_text = help_txt_passwd1
        help_txt_passwd2 = '''Entrez le même mot de passe que précédemment.'''

        self.fields['password2'].label = "Confirmation du mot de passe"
        self.fields['password2'].help_text = help_txt_passwd2




class UserRegistrationView(CreateView):
    #form_class = UserCreationForm
    form_class = MyUserCreationForm
    template_name = 'accounts/user_registration.html'
    
    def get_success_url(self):
        return reverse('home')



