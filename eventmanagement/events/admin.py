from django.contrib import admin

from .models import Category, Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'text',
                    'date',
                    'time',
                    'category')
    search_fields = ('name', 'category')
    empty_value_display = '-пусто-'


admin.site.register(Event, EventAdmin)
admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'slug')
    search_fields = ('name', )
