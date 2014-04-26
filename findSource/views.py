#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from findSource.AlchemyTest.processdata import readJson
from findSource.AlchemyTest.processdata import calTerm
from findSource.AlchemyTest.processdata import  buildGraph
# Create your views here.

class IndexView(TemplateView):
    template_name = 'findSource/index.html'

    def get_terms(self):
        list_term = readJson('terms')
        return list_term

    def get_subjects(self):
        list_subject = readJson('subjects')
        return list_subject

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['subjects'] = self.get_subjects()      
        context['terms'] = self.get_terms()             
        return context

class ResultView(TemplateView):
    template_name = 'findSource/result.html'

    def get_queryset(self):
        key_word = self.kwargs['key_word']
        return key_word

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        key_word = self.get_queryset()
        context['key_word'] = key_word

        term = self.kwargs['term']
        context['term'] = term

        context['term_id'] = calTerm (term)
        return context

class AboutView(TemplateView):
    template_name = 'findSource/about.html'
