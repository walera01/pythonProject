from django.shortcuts import render, HttpResponse
from .forms import Forma
from .models import *

def site1(request):
    form = Forma(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data= form.cleaned_data
        new_form = form.save()
    return render(request, 'djamshut/reqister.html', locals())

def site2(request):
    form = Regis.objects.all()
    cats = Category.objects.all()
    context = {
        'form': form,
        'cats': cats,
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
    form = Regis.objects.filter(id=cat_id)
    cats=Category.objects.all()

    context = {
        'form': form,
        'cat_id': cat_id,
        'cats': cats,
        'cat_selected': cat_id,
    }
    return render(request, 'djamshut/client.html',context=context)