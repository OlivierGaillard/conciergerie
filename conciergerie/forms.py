from datetime import datetime
from django import forms
from conciergerie.models import Travail


class TravailCreateForm(forms.ModelForm):
    datefr = forms.DateField(widget=forms.DateInput(
        format='%d.%m.%Y',
        attrs={'class' : 'form-control'},
        ), 
        #initial=datetime.today,
    )


    class Meta:
        model = Travail
        fields = ['datefr', 'type', 'titre', 'temps' ]
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
        widgets = {
            'temps' : forms.TextInput(attrs={'class': 'form-control'}),
            'titre' : forms.TextInput(attrs={'class': 'form-control'}),
        }