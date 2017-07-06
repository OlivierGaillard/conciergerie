from django.shortcuts import reverse
from django.views.generic import CreateView, ListView
from menages.forms import WorkForm, SejourForm, TissueForm, TissueCategoryForm, WorkCategoryForm
from menages.models import Sejour, Work, TissueCategory, Tissue, WorkCategory
# Create your views here.

class SejourCreateView(CreateView):
    model = Sejour
    form_class = SejourForm
    template_name = 'menages/sejour.html'

    def get_success_url(self):
        return reverse('menages:sejours')

class SejourListView(ListView):
    model = Sejour
    template_name = 'menages/sejours.html'
    context_object_name = 'liste'

class WorksListView(ListView):
    model = Work
    context_object_name = 'travaux'
    template_name = 'menages/works.html'

class WorkCreateView(CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'menages/work.html'

    def get_success_url(self):
        return reverse('menages:works')


class TissueCategoryListView(ListView):
    model = TissueCategory
    template_name = 'menages/categories_tissus.html'
    context_object_name = 'categories'


class TissueCategoryCreateView(CreateView):
    model = TissueCategory
    form_class = TissueCategoryForm
    template_name = 'menages/categorie_tissu.html'

    def get_success_url(self):
        return reverse('menages:tissuscatego')

class WorkCategoryListView(ListView):
    model = WorkCategory
    template_name = 'menages/categories_travaux.html'
    context_object_name = 'categories'

class WorkCategoryCreateView(CreateView):
    model = WorkCategory
    form_class = WorkCategoryForm
    template_name = 'menages/categorie_travail.html'

    def get_success_url(self):
        return reverse('menages:workcategories')

class TissueListView(ListView):
    model = Tissue
    context_object_name = 'tissus'
    template_name = 'menages/tissus.html'

class TissueCreateView(CreateView):
    model = Tissue
    form_class = TissueForm
    template_name = 'menages/tissu.html'
    context_object_name = 'tissu'

    def get_success_url(self):
        return reverse('menages:tissus')






