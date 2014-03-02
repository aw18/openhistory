# This is the URLconf for ohapp
# @albertina

from django.conf.urls import patterns, url
from ohapp import views

urlpatterns = patterns('',
    url(r'^base$', views.base, name="base"),
    url(r'^$', views.index, name="index"),
    url(r'^p1$', views.p1, name="p1"),
    url(r'^team$', views.team, name="team"),
)
