from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import calendar
from .models import Event
from datetime import date


def home(request):
    return render(request, 'front_end.html')

def CalendarApp(request):
    jan = calendar.month(2023,1)
    print(jan)
    return HttpResponse(jan)

def get_calendar(request):
    print("Get calendar function called")
    year = int(request.GET.get('year', 2023))  # Get year from request, default to 2023
    month = int(request.GET.get('month', 1))  # Get month from request, default to January

    cal = calendar.HTMLCalendar().formatmonth(year, month)
    
    return JsonResponse({'calendar': cal})  # Return as JSON

def create_event(request):
    # Example: Creating an event (this can be replaced with form handling)
    print('Here')
    New_Event = request.GET.get('title')
    desc = request.GET.get('description')
    print(New_Event,desc)
    Event.objects.create(title=New_Event, description=desc, date=date.today())
    return HttpResponse("Event Created Successfully!")

def list_events(request):
    print('Here')
    events = Event.objects.all().values('title', 'description', 'date')
    print(list(events),events)
    return JsonResponse({'events': list(events)})  # Return JSON for AJAX calls

