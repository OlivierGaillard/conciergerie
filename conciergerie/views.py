from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.shortcuts import render, reverse
from django.views.generic import CreateView, TemplateView
from crispy_forms.layout import Submit
from django_filters.views import FilterView
from .models import Travail
from .filters import TravailFilter
from .forms import TravailCreateForm, TravailFormSetHelper

class  TravailCreateView(CreateView):
    model = Travail
    template_name = "conciergerie/create.html"
    form_class = TravailCreateForm
    extra_forms = 8
    TravailFormset = modelformset_factory(Travail,
                                          fields=['date', 'titre', 'temps'],
                                          form=TravailCreateForm,
                                          can_delete=True,
                                          max_num=10,
                                          extra=extra_forms)

    def make_crispy_helper(self):
        helper = TravailFormSetHelper()
        helper.add_input(Submit("submit", "Save"))
        helper.label_class = 'col-sm-2'
        helper.field_class = 'col-sm-2'
        helper.template = 'bootstrap/table_inline_formset.html'
        return helper

    def get_context_data(self, **kwargs):
        context = super(TravailCreateView, self).get_context_data(**kwargs)
        formset = self.TravailFormset()
        context['formset'] = formset
        context['helper'] = self.make_crispy_helper()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        formset = self.TravailFormset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('conciergerie:list'))
        else:
            context = super(TravailCreateView, self).get_context_data(**kwargs)
            context['formset'] = formset
            context['helper'] = self.make_crispy_helper()
            return render(request, template_name=self.template_name, context=context)

    def get_success_url(self):
        return reverse('conciergerie:list')



class TravailListViewFiltered(FilterView):
    filterset_class = TravailFilter
    template_name = "conciergerie/list.html"

    def get_context_data(self, **kwargs):
        context = super(TravailListViewFiltered, self).get_context_data(**kwargs)
        temps_total = 0
        for i in self.filterset.qs:
            temps_total += i.temps
        context['temps_total'] = temps_total
        return context


class AboutView(TemplateView):
    template_name = 'conciergerie/about.html'





