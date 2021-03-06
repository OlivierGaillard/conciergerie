from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.forms import modelformset_factory
from django.forms.models import BaseModelFormSet
from django.forms.formsets import DELETION_FIELD_NAME
from django.shortcuts import render, reverse
from django.views.generic import CreateView, TemplateView
from django_filters.views import FilterView
from .models import Travail, Salary
from .filters import TravailFilter
from .forms import TravailCreateForm


class BaseTravailFormSet(BaseModelFormSet):

    def add_fields(self, form, index):
        super(BaseTravailFormSet, self).add_fields(form, index)
        form.fields[DELETION_FIELD_NAME].label = 'Effacer'



@method_decorator(login_required, name='dispatch')
class  TravailCreateView(CreateView):
    model = Travail
    template_name = "conciergerie/create.html"
    form_class = TravailCreateForm
    extra_forms = 10
    TravailFormset = modelformset_factory(Travail,
    fields=['datefr', 'type', 'titre', 'temps'],
                                          form=TravailCreateForm,
                                          formset=BaseTravailFormSet,
                                          can_delete=True,
                                          max_num=30,
                                          extra=extra_forms)




    def get_context_data(self, **kwargs):
        context = super(TravailCreateView, self).get_context_data(**kwargs)
        q1 = Travail.objects.filter(owner=self.request.user)
                                             #).filter(datefr__month=datetime.today().month)
        formset = self.TravailFormset(queryset=q1)
        context['formset'] = formset
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        formset = self.TravailFormset(request.POST, request.FILES)
        if formset.is_valid():
            i=0
            instances = formset.save(commit=False)
            for travail in instances:
                i += 1
                travail.owner  = self.request.user
                travail.save()
            for obj in formset.deleted_objects:
                obj.delete()
            return HttpResponseRedirect(reverse('conciergerie:list'))
        else:
            context = super(TravailCreateView, self).get_context_data(**kwargs)
            context['formset'] = formset
            return render(request, template_name=self.template_name, context=context)


    def get_success_url(self):
        return reverse('conciergerie:list')


@method_decorator(login_required, name='dispatch')
class TravailListViewFiltered(FilterView):

    filterset_class = TravailFilter
    template_name = "conciergerie/list.html"

    def get_context_data(self, **kwargs):
        context = super(TravailListViewFiltered, self).get_context_data(**kwargs)
        temps_total = 0
        owner = self.request.user
        for i in self.filterset.qs:
            temps_total += i.temps
        context['temps_total'] = temps_total
        context['owner'] = owner
        hour_salary = Salary.objects.get(owner=self.request.user).hour_amount
        context['salaire_horaire'] = hour_salary
        context['salaire'] = hour_salary * temps_total
        return context


class AboutView(TemplateView):
    template_name = 'conciergerie/about.html'





