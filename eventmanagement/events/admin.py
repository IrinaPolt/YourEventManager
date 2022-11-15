from django.contrib import admin
from .models import Event, Category


class EventAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'text',
                    'datetime')
    search_fields = ('name', )
    empty_value_display = '-пусто-'


admin.site.register(Event, EventAdmin)
admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'slug')
    search_fields = ('name', )