from django.conf.urls import url
from . import views

app_name = "menages"
urlpatterns = [
    url(r'^sejour$',  views.SejourCreateView.as_view(), name='sejour'),
    url(r'^sejours$',  views.SejourListView.as_view(), name='sejours'),
    url(r'travail', views.WorkCreateView.as_view(), name='work'),
    url(r'tissuscategories$', views.TissueCategoryListView.as_view(), name='tissuscatego'),
    url(r'categorie$', views.TissueCategoryCreateView.as_view(), name='categorie',),
    url(r'tissu$', views.TissueCreateView.as_view(), name='tissu'),
    url(r'tissus$', views.TissueListView.as_view(), name='tissus'),
    url(r'works$', views.WorksListView.as_view(), name='works'),
    url(r'workcategories$', views.WorkCategoryListView.as_view(), name='workcategories'),
    url(r'workcategory$', views.WorkCategoryCreateView.as_view(), name='workcategory'),
]