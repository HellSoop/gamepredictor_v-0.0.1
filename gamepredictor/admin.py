from django.contrib import admin
from .models import *

class GamepredictorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cover']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']

admin.site.register(Games, GamepredictorAdmin)
