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
    context = {
        'form': form,
    }
    return render(request, 'djamshut/clients.html', context=context)

def name_id(request, form_id):
    return HttpResponse(f"name number {form_id}")