from django.shortcuts import render, reverse
from django.views.generic import CreateView, TemplateView
from django.views import View
from django_filters.views import FilterView
from .models import Travail
from .filters import TravailFilter
from .forms import TravailCreateForm, TravailFilterForm

# Create your views here.
class TravailCreateView(CreateView):
    model = Travail
    template_name = "conciergerie/create.html"
    form_class = TravailCreateForm

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
        # arrivage = self.request.GET.get('arrivage_ref', '')
        # if len(arrivage) > 0:
        #     print("ArrivageID: %s" % arrivage)
        # devises = Currency.objects.all()
        # monnaie = 'XOF'
        # monnaie = self.request.GET.get('monnaie', '')
        # if len(monnaie) == 0:
        #     monnaie = 'XOF'
        # total =0
        # devise_total = monnaie
        # converter = Converter()
        # for i in self.filterset.qs:
        #     if i.devise_id.currency_code == devise_total:
        #         total += i.montant
        #         i.montantTargetAmount = i.montant
        #     else:
        #         montant_target = i.convert(monnaie)
        #         i.montantTargetAmount = montant_target.amount
        #         total += montant_target.amount
        #
        # context['total'] = total
        # context['devise_total'] = devise_total
        # context['total_target'] = total
        # context['devises'] = devises
        # if self.filterset.qs:
        #     context['last_arrivage_ref'] = self.filterset.qs.last().arrivage_ref
        # else:
        #     context['arrivageID'] = arrivage
        return context


class AboutView(TemplateView):
    template_name = 'conciergerie/about.html'





