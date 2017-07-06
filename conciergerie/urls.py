from django.conf.urls import url
from . import views

app_name = "conciergerie"

urlpatterns = [
    url(r'^about$', views.AboutView.as_view(), name='about'),
    url(r'^createtv$',  views.TravailCreateView.as_view(), name='createtv'),
    url(r'^list$',  views.TravailListViewFiltered.as_view(), name='list'),
]