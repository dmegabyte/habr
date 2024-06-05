from django.shortcuts import render
from django.shortcuts import HttpResponse
from main.models import Room

# Create your views here.


def index(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
        
    }

    return render(request, 'index.html', context)

def room(request):
    return HttpResponse("room.html")

