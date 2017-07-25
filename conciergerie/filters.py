from datetime import datetime
from django_filters import FilterSet
import django_filters
from .models import Travail
#from .forms import TravailFilterForm


class TravailFilter(FilterSet):

    mois_sel = (
        (1, 'janvier'), (2, 'février'), (3, 'mars'), (4, 'avril'), (5, 'mai'),
        (6, 'juin'), (7, 'juillet'), (8, 'août'), (9, 'sept'), (10, 'oct'),
        (11, 'novembre'), (12, 'décembre')
                )
    month = django_filters.ChoiceFilter(label='Mois', name='datefr', lookup_expr='month',
                                        choices=mois_sel)
    choices = ('C', 'Conciergerie'), ('A', 'AirBnB')
    type_travail = django_filters.ChoiceFilter(label='Type de travail', name='type', choices=choices)

    class Meta:
        model = Travail
        fields = []
        #form = TravailFilterForm

    @property
    def qs(self):
        parent = super(TravailFilter, self).qs
        d = datetime.now()
        return parent.filter(owner=self.request.user, datefr__year=d.year)

