from django import forms
from .models import Event, Category


class EventForm(forms.ModelForm):
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    datetime = forms.DateTimeField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                   required=False)

    class Meta:
        model = Event
        fields = ['name', 'text', 'datetime', 'category']
        label = {
            'name': 'Название мероприятия',
            'text': 'Описание',
            'datetime': 'Дата и время проведения',
            'category': 'Категория мероприятия'
        }