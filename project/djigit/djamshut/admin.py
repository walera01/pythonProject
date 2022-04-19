from django.contrib import admin
from .models import *

class RegisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category_id')
    list_display_links = ('id', 'name')

admin.site.register(Regis, RegisAdmin)
admin.site.register(Category)

