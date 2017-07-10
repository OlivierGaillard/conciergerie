from django import forms
from django.shortcuts import reverse
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from conciergerie.models import Travail
#from .filters import TravailFilter

class TravailCreateForm(forms.ModelForm):

    class Meta:
        model = Travail
        fields = ['date', 'titre', 'temps' ]
        widgets = {
            'date': forms.TextInput(
                attrs={'type': 'date'},
            ),
        }

        error_messages = {
            'temps' : { 'invalid': 'Pas valide',
                        'required' : 'Ce champ est requis',
                        'max_digits' : "Pas plus de 1 chiffre avant la virgule et 2 après",
                        'max_decimal_places' : "Pas plus de 2 décimales",
                        'max_whole_digits' : "Pas plus de 1 chiffre entier",
                        },
            'date' : {
                'required': 'Ce champ est requis',
                'invalid' : 'Entrez une date valide',
            },
            'titre' : {
                'required': 'Ce champ est requis',
            }

        }

class TravailFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TravailFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_action = reverse('conciergerie:createtv')
        self.layout = Layout(
            'date',
            'titre',
            'temps',
        )

        self.render_required_fields = False



class TravailFilterForm(forms.Form):
    date = forms.DateField(label='Date travail',
                                    widget=forms.TextInput(attrs={'type': 'date'})
                                    )

    def __init__(self, *args, **kwargs):
        super(TravailFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = "POST"
        self.helper.form_action = reverse('conciergerie:list')
        self.helper.add_input(Submit('Submit', 'submit'))