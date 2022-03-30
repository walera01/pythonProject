from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

admin.autodiscover()

urlpatterns = [
    path('qwe/', views.admin1, name='first'),
    path('thanks/', views.admin2, name='second')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
