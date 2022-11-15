from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('create/', views.event_create, name='event_create'),
    path('events/<event_id>/edit/', views.event_edit, name='event_edit'),
    path('profile/<username>/', views.profile, name='profile'),
    path('events/<event_id>/', views.event_detail, name='event_detail'),
    path('category', views.event_list),
    path('category/<slug>/', views.category_events, name='category_list'),
    path('', views.index, name='index'),
]