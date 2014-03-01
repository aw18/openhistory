# This is the URLconf for ohapp
# @albertina

from django.conf.urls import patterns, url
from ohapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index")
)
