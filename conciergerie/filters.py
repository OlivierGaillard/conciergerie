from datetime import datetime
from django_filters import FilterSet
import django_filters
from .models import Travail
from .forms import TravailFilterForm


class TravailFilter(FilterSet):
    month = django_filters.NumberFilter(label='No du mois', name='datefr', lookup_expr='month')
    choices = ('C', 'Conciergerie'), ('A', 'AirBnB')
    type_travail = django_filters.ChoiceFilter(label='Type de travail', name='type', choices=choices)

    class Meta:
        model = Travail
        fields = []
        form = TravailFilterForm

    @property
    def qs(self):
        parent = super(TravailFilter, self).qs
        d = datetime.now()
        return parent.filter(owner=self.request.user, datefr__year=d.year)

