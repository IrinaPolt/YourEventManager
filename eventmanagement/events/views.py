from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Category
from .forms import EventForm

PAGE_NMB = 10

User = get_user_model()


def index(request):
    event_list = Event.objects.all().order_by('-pk')
    paginator = Paginator(event_list, PAGE_NMB)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'event_list': event_list,
        'page_obj': page_obj,
    }
    return render(request, 'events/index.html', context)


def category_list(request):
    return render(request, 'events/category_list.html')


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    events = category.events.all().order_by('-pk')
    paginator = Paginator(events, PAGE_NMB)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'category': category,
        'events': events,
    }
    return render(request, 'events/category_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    events = author.events.all()
    events_count = events.count()
    paginator = Paginator(events, PAGE_NMB)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'events': events,
        'page_obj': page_obj,
        'events_count': events_count,
    }
    return render(request, 'events/profile.html', context)


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    author = event.author
    events_count = author.events.count()
    context = {
        'event': event,
        'author': author,
        'events_count': events_count,
    }
    return render(request, 'events/event_detail.html', context)


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('events:profile',
                            username=event.author)
        return render(request, 'events/create_event.html',
                      {'form': form})
    else:
        form = EventForm()
        return render(request, 'events/create_event.html',
                      {'form': form})


def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    is_edit = True
    if request.user != event.author:
        return redirect('events:event_detail', event.pk)
    if request.method != 'POST':
        form = EventForm(instance=event)
        return render(request, 'events/create_event.html',
                      {'form': form, 'is_edit': is_edit, 'event': event})
    form = EventForm(request.POST, instance=event)
    if form.is_valid():
        event = form.save(commit=False)
        event.category = event.category
        event.save()
        return redirect('events:event_detail',
                        event_id=event.id)
    return render(request, 'events/create_event.html',
                  {'form': form, 'is_edit': is_edit, 'event': event})