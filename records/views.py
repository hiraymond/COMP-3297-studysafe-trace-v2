from django.shortcuts import render
from sqlite3 import connect
import requests
import json
from django.http import HttpResponse

def view_contacts(request, hku_id, date):
    try:
        url = 'https://comp-3297-studysafe.herokuapp.com/records/'+hku_id+'/contacts?date='+date
        resp1 = requests.get(url)
        bool_connected = True
    except requests.exceptions.ConnectionError:
        bool_connected = False

    if (bool_connected):
        result = resp1.json()

    context = {"subject": hku_id, "date": date, "contacts": result}
    return render(request, 'contacts.html', context=context)

def view_venues(request, hku_id, date):
    try:
        url = 'https://comp-3297-studysafe.herokuapp.com/records/'+hku_id+'/venues?date='+date
        resp2 = requests.get(url)
        bool_connected = True
    except requests.exceptions.ConnectionError:
        bool_connected = False

    if (bool_connected):
        result = resp2.json()

    context = {"subject": hku_id, "date": date, "venues": result}
    return render(request, 'venues.html', context=context)