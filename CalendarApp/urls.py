from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
     path('get-calendar/', views.get_calendar, name='get_calendar'),
     path('create-event/', views.create_event, name='create_event'),
     path('list-events/', views.list_events, name='list_events')
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)