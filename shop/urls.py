
#shop/urls.py
from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns=[
    url(r'^$', views.all),
    #url(r'^(?P<id>\d+)/$', views.post_detail),
    #url(r'^post/(?P<id>\d+)/$', views.post_list),
 ]
