from django.shortcuts import render

def events(request):
    return render(request, 'events/events.html')

def eventcreate(request):
    return render(request, 'events/eventcreate.html')
