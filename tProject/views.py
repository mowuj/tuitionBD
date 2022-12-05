from django.shortcuts import render,HttpResponse

from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name= 'home.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['msg']='Welcome to our website'
        context['msg2'] = 'Welcome to our website again'
        return context
