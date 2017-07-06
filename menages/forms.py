from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms import layout
from crispy_forms import bootstrap
from django import forms
from django.shortcuts import reverse
from mptt.forms import TreeNodeChoiceField, TreeNodeMultipleChoiceField
from .fields import MultipleChoiceTreeField
from .models import Sejour,   Work, Tissue, TissueCategory, WorkCategory


class SejourForm(forms.ModelForm):

    class Meta:
        model = Sejour
        fields = ['visiteur', 'arrivee', 'depart']
        widgets = {
            'arrivee' : forms.TextInput(
                attrs={'type':'date'}
            ),
            'depart': forms.TextInput(
                attrs={'type': 'date'}
            )

        }

    def __init__(self, *args, **kwargs):
        super(SejourForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        #self.helper.label_class = 'col-lg-2'
        #self.helper.field_class = 'col-lg-5'
        self.helper.form_id = 'id-sejour-form'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('menages:sejour')
        self.helper.layout = Layout(
            'visiteur',
            'arrivee',
            'depart',
        )
        self.helper.add_input(Submit('submit', 'Submit'))



class WorkForm(forms.ModelForm):
    work_category = TreeNodeMultipleChoiceField(queryset=WorkCategory.objects.all(),
                                                label='Type')

    class Meta:
        model = Work
        fields = ['sejour', 'work_category', 'work_name', 'heure', 'minutes', 'quantity',]

    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('menages:work')
        self.helper.add_input(Submit('submit', 'Submit'))

class TissueForm(forms.ModelForm):
    tissuecategory = TreeNodeChoiceField(queryset=TissueCategory.objects.all(),
                                                    label='Genre de tissu',
                                           to_field_name='title')

    class Meta:
        model = Tissue
        fields = ['name', 'tarif', 'tissuecategory']


    def __init__(self, *args, **kwargs):
        super(TissueForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('menages:tissu')
        self.helper.add_input(Submit('submit', 'Submit'))


class WorkCategoryForm(forms.ModelForm):
    #work_category = TreeNodeMultipleChoiceField(queryset=WorkCategory.objects.all(),
   #                                            label='Type')
    # workcategory = MultipleChoiceTreeField(
    #     label='Type',
    #     queryset=WorkCategory.objects.all(),
    # )

    class Meta:
        model = WorkCategory
        fields = ['parent', 'title']

    def __init__(self, *args, **kwargs):
        super(WorkCategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.form_action = reverse('menages:workcategory')
        self.helper.add_input(Submit('submit', 'Submit'))


class TissueCategoryForm(forms.ModelForm):

    class Meta:
        model = TissueCategory
        fields = ['parent', 'title', ]


    def __init__(self, *args, **kwargs):
        super(TissueCategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse('menages:categorie')
        self.helper.add_input(Submit('submit', 'Submit'))




