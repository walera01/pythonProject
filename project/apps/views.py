from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Lucky
from .models import Subs


def admin1(request):
    form = Lucky(request.POST or None)
    user = Subs.objects.all()
   # delete = user.delete()
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()
        new_form.save()
        print(request.POST)
        print(data['name'])
        return render(request, 'apps/admin2.html')
    return render(request, "apps/admin1.html", locals())

def admin2(request):
    return render(request, 'apps/admin2.html')
