from django.shortcuts import render


def home(request):
    events = get_events()
    return render(request, 'event.html', {'events': events})
from bs4 import BeautifulSoup
import requests


def get_events():
    response = requests.get('https://allevents.in/sydney')

    event = response.text

    soup = BeautifulSoup(event, 'html.parser')

    event_tag = soup.find_all(name="div", class_="title")

    events = []
    for ev in event_tag:
        event_title = ev.getText()
        event_link = ev.find('a')
        link = event_link['href']
        
        
       
        events.append({"title": event_title, "link": link})
    return events 