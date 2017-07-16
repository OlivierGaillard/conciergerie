from django import forms
from django.shortcuts import reverse
from crispy_forms.helper import FormHelper, Layout
from conciergerie.models import Travail

#from .filters import TravailFilter

class TravailCreateForm(forms.ModelForm):
    date = forms.DateField(input_formats=["%d/%m/%Y","%d.%m.%Y","%d-%m-%Y"], help_text="exemple: 30/12/2017")    #input_formats=["%d/%m/%Y",], )

    #date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}), required=True, input_formats=['%d/%m/%Y', ])

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
    #month = forms.IntegerField(min_value=1, max_value=12)

    def clean(self):
        cleaned_data = super(TravailFilterForm,self).clean()
        year = cleaned_data.get("year")
        if year and (year < 2017 or year > 2020):
            self._errors['year'] = self._errors.get('year', [])
            self._errors['year'].append("Choisir une valeur entre 2017 et 2019 (pour l'instant...)")

        month = cleaned_data.get("month")
        if month is not None:
            if month < 1 or month > 12:
                self._errors['month'] = self._errors.get('month', [])
                self._errors['month'].append("Choisir une valeur entre 1 et 12")

        return cleaned_data
