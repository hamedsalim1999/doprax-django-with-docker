from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import ThreadForm, ReplyForm
from .models import Thread,Reply
from django.views.generic import FormView,DetailView
from django.shortcuts import get_object_or_404
from django.contrib import messages
class ThreadFormSend(FormView):
    template_name = 'forum/index.html'
    form_class = ThreadForm
    success_url = '/success/'
    def get_context_data(self, *args,**kwargs):
        context = super(ThreadFormSend,self).get_context_data(*args,**kwargs)
        context["threads"] = Thread.objects.all()
        return context

class ThreadView(DetailView):
    template_name = 'forum/thread.html'
    model = Thread
    context_object_name = 'thread'
    slug_url_kwarg ='slug'
    def get_context_data(self, *args,**kwargs):
        context = super(ThreadView,self).get_context_data(*args,**kwargs)
        context["replay"] = Reply.objects.filter(thread=context['thread'])
        return context
    
class new_thread(FormView):
    form_class  = ThreadForm
    model = Thread
    success_url = 'index'
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)
class new_replay(FormView):
    form_class  =ReplyForm
    model = Reply
    success_url = 'index'
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)