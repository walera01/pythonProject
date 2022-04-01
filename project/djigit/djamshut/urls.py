from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.autodiscover()

urlpatterns = [
    path('register/', views.site1, name='home'),
    path('client/', views.site2, name='second'),
    path('form/<int:form_id>/', views.name_id, name="form"),
    path('category/<int:cat_id>/', views.name_id2, name='category')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)