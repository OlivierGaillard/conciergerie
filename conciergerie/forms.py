from django import forms
from django.shortcuts import reverse
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from conciergerie.models import Travail
#from .filters import TravailFilter

class TravailCreateForm(forms.ModelForm):

    class Meta:
        model = Travail
        fields = ['date', 'titre', 'temps', ]
        widgets = {
            'date': forms.TextInput(
                attrs={'type': 'date'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(TravailCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-2'
        self.helper.field_class = 'col-sm-3'
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('conciergerie:createtv')
        self.helper.add_input(Submit('submit', 'Submit'))


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