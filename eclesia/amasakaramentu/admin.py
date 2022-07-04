from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(amsakaramentu)
class amasakaramentu(admin.ModelAdmin):
    list_display = ['natus','nomen','pater','mater','baptizus','com_prima','com_solen','confirmatis','matrimonium','status']
    # ordering = ['client','dateAtri']
