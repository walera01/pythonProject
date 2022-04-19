import this

from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView

from .forms import Forma
from .models import *

class Site1(CreateView):
    form_class = Forma
    template_name = 'djamshut/reqister.html'
    success_url = reverse_lazy('home')

class Site(ListView):
    model = Regis
    template_name = 'djamshut/clients.html'
    context_object_name = 'form'


def site2(request, d=0):
    form = Regis.objects.all()
    if d==1:
        form.delete()
        return HttpResponse('<h1>form is delete</h1><a href="/client/">Ok </a>')
    context = {
        'form': form,
    }
    return render(request, 'djamshut/clients.html', context=context)


def name_id(request, form_id):
    form = Regis.objects.filter(id=form_id)
    context = {
        'form': form,
        'form_id': form_id,
    }
    return render(request, 'djamshut/nameclient.html',context=context)


def name_id2(request, cat_id):
    form = Regis.objects.filter(category_id=cat_id)
    context = {
        'form': form,
        'cat_id': cat_id,
        'cat_selected': cat_id,
    }
    return render(request, 'djamshut/clients.html',context=context)