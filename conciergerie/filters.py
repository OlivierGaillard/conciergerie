import django_filters
from django_filters.widgets import RangeWidget
from django import forms
from .models import Travail
from .forms import TravailFilterForm

class TravailFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'MM/JJ/YYYY',
                                                                          'type': 'date'}
                                                                          )
                                                )
    #DateFromToRangeFilter(widget=RangeWidget(attrs={'placeholder': 'YYYY/MM/DD'}))

    class Meta:
        model = Travail
        fields = ['date']
        widgets = {
            'date': forms.TextInput(
                attrs={'type': 'date'}
            ),
        }
        #form = TravailFilterForm
