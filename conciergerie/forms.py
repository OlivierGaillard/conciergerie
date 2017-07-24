from datetime import datetime
from django import forms
from conciergerie.models import Travail


class TravailCreateForm(forms.ModelForm):
    datefr = forms.DateField(widget=forms.DateInput(
        format='%d.%m.%Y',
        attrs={'readonly' : 'readonly'},
        ),
        #initial=datetime.today,
    )


    class Meta:
        model = Travail
        fields = ['datefr', 'titre', 'temps' ]
        error_messages = {
            'temps' : { 'invalid': 'Format pas valide. Une virgule et non un point?',
                        'required' : 'Entrez une duree',
                        'max_digits' : "Pas plus de 1 chiffre avant la virgule et 2 après",
                        'max_decimal_places' : "Pas plus de 2 décimales",
                        'max_whole_digits' : "Pas plus de 1 chiffre entier",
                        },
            'datefr' : {
                'required': 'Une date svp',
                'invalid' : 'Entrez une date valide',
            },
            'titre' : {
                'required': 'Entrez une description du travail',
            }

        }





class TravailFilterForm(forms.Form):

    def clean(self):
        cleaned_data = super(TravailFilterForm,self).clean()
        month = cleaned_data.get("month")
        if month is not None:
            if month < 1 or month > 12:
                self._errors['month'] = self._errors.get('month', [])
                self._errors['month'].append("Choisir une valeur entre 1 et 12")

        return cleaned_data
