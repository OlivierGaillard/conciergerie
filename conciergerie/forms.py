from django import forms
from django.shortcuts import reverse
from crispy_forms.helper import FormHelper, Layout
from conciergerie.models import Travail

#from .filters import TravailFilter

class TravailCreateForm(forms.ModelForm):
    date = forms.DateField(help_text="exemple: 30/12/2017 ou 30.12.17 ou 30 12 17; 30 1 17 etc: jour mois année")


    class Meta:
        model = Travail
        fields = ['date', 'titre', 'temps' ]
        error_messages = {
            'temps' : { 'invalid': 'Format pas valide. Une virgule et non un point?',
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

    def clean(self):
        cleaned_data = super(TravailFilterForm,self).clean()
        month = cleaned_data.get("month")
        if month is not None:
            if month < 1 or month > 12:
                self._errors['month'] = self._errors.get('month', [])
                self._errors['month'].append("Choisir une valeur entre 1 et 12")

        return cleaned_data
