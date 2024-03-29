# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from findSource import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^about$', views.AboutView.as_view(), name = 'about'),
        url(r'^(?P<key_word>.*)/(?P<term>.*)$', views.ResultView.as_view(), name='result'),
        url(r'^(?P<key_word>.*)/(?P<term>.*)$', views.ResultsView.as_view(), name='results'),        
)

urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^/static/(?P<path>.*)$', 'serve'),
    )

