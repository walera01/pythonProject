from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.autodiscover()

urlpatterns = [
    path('register/', views.site1, name='first'),
    path('client/', views.site2, name='second'),
    path('form/<int:form_id>/', views.name_id, name="form")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)