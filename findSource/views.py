#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from findSource.AlchemyTest.processdata import readJson

from findSource.AlchemyTest.calTermId import calTerm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'findSource/index.html'

    def get_queryset(self):
        list = readJson()
        # print list
        return list


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['result'] = self.get_queryset()        
        return context

class ResultView(ListView):
    template_name = 'findSource/result.html'

    def get_queryset(self):
        url = self.kwargs['userInput']
        # list = readJson(url)
        # #print list
        # return list

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        department = self.kwargs['department']
        context['department'] = department

        year = self.kwargs['year']
        context['year'] = year

        quater = self.kwargs['quater']
        context['quater'] = quater

        context['term_id'] = calTerm (year,quater)

        return context

class AboutView(TemplateView):
    template_name = 'findSource/about.html'
