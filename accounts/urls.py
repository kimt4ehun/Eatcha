from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns =[
    url(r'^profile/$', views.profile,  name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login', kwargs={'template_name': 'accounts/login_form.html'}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^login/$', auth_views.login, name='login', kwargs={'authentication_form': LoginForm,'template_name': 'accounts/login_form.html',}),

] #Kwang=keywardargments