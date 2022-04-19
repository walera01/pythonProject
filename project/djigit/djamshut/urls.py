from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

admin.autodiscover()

urlpatterns = [
    path('register/',Site1.as_view(), name='home'),
    path('client/', Site.as_view(), name='second'),
    path('form/<int:form_id>/', views.name_id, name="form"),
    path('category/<int:cat_id>/', views.name_id2, name='category'),
    path('delete/<int:d>/', views.site2, name='second'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)