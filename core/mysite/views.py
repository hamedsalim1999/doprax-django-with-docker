from django.db.models.base import Model
from django.db.models.indexes import Index
from .models import Contact,Info,Slider
from .forms import ContactUs
from django.shortcuts import render,get_object_or_404
from django.views.generic import View,ListView,DetailView,CreateView,TemplateView,FormView
from django.contrib.messages.views import SuccessMessageMixin

class Index(TemplateView):
    template_name = 'mysite/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.objects.all()
        return context
class About(TemplateView):
    template_name = 'mysite/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.objects.all()
        return context

class contact_form(SuccessMessageMixin,CreateView):
    template_name = 'mysite/contact.html'
    form_class  = ContactUs
    model = Contact
    success_url ="/contact"
    success_message = 'Everything is fine'
