from django.contrib import admin
from .models import Animal_Log, Animals

# Register your models here.
@admin.register(Animal_Log)
class AnimalLogAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'loc')

@admin.register(Animals)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name']