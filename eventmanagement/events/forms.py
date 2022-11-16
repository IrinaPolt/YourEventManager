from django import forms
from django.contrib.admin import widgets

from .models import Category, Event


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]


class EventForm(forms.ModelForm):
    name = forms.CharField()
    text = forms.CharField(widget=widgets.AdminTextareaWidget)
    date = forms.DateField(widget=forms.SelectDateWidget)
    time = forms.TimeField(widget=forms.TimeInput)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = Event
        fields = ['name', 'text', 'date', 'time', 'category', 'image']
        label = {
            'name': 'Название мероприятия',
            'text': 'Описание',
            'date': 'Дата проведения',
            'time': 'Время проведения',
            'category': 'Категория мероприятия',
            'image': 'Изображение'
        }
