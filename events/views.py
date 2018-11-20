from django.shortcuts import render, redirect, get_object_or_404
# creating login required
from django.contrib.auth.decorators import login_required
# importing model Product from models
from .models import Event
from django.utils import timezone

def events(request):
    event = Event.objects
    return render(request, 'events/events.html', {'events':event})

@login_required(login_url="/accounts/signup")
def eventcreate(request):
    #check if it is post request
    if request.method == 'POST':
        #passing needed Product model attributes
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            #creating product in DB
            event = Event()
            event.title = request.POST['title']
            event.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                event.url = request.POST['url']
            else:
                event.url = 'http://' + request.POST['url']
            event.icon = request.FILES['icon']
            event.image = request.FILES['image']
            event.pub_date = timezone.datetime.now()
            event.author = request.user
            #insert product in DB
            event.save()
            #redirecting to products/product_id
            return redirect("home")
    else:
        return render(request, 'events/eventcreate.html', {'error':'All fields are required.'})
    return render(request, 'events/eventcreate.html')

def detail(request, product_id):
    event = get_object_or_404(Event, pk=product_id)
    return render(request, 'events/detail.html', {'event':events})
