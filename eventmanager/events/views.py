from django.shortcuts import render, redirect
from events.scraping import get_events

from .models import EmailCapture
from django.views.decorators.csrf import csrf_exempt


def home(request):
    events = get_events()
    return render(request, 'event.html', {'events': events})


def event_list(request):
    # Your existing scraping logic or data
    events = [...]  # List of dicts with 'title', 'description', 'link'
    return render(request, 'event.html', {'events': events})

@csrf_exempt
def get_ticket(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        event_link = request.POST.get('event_link')
        if email and event_link:
            EmailCapture.objects.create(email=email, event_link=event_link)
            return redirect(event_link)
    event_link = request.GET.get('event_link')
    return render(request, 'email_form.html', {'event_link': event_link})