from django import forms
from django.contrib.admin import widgets 
from .models import Event, Category


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]

class EventForm(forms.ModelForm):
    name = forms.CharField()
    text = forms.CharField(widget=widgets.AdminTextareaWidget)
    #mydate = forms.DateField(widget=widgets.AdminDateWidget)
    #mytime = forms.TimeField(widget=widgets.AdminTimeWidget)
    datetime = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                   required=False)
    image = forms.ImageField(widget=widgets.AdminFileWidget)

    class Meta:
        model = Event
        fields = ['name', 'text', 'datetime', 'category']
        label = {
            'name': 'Название мероприятия',
            'text': 'Описание',
            'datetime': 'Дата и время проведения',
            'category': 'Категория мероприятия'
        }