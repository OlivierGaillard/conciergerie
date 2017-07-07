from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^new-user/$',  views.UserRegistrationView.as_view(), name='user_registration'),
    ]
