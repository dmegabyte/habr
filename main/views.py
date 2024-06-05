from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from main.models import Room

# Create your views here.


def index(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
        
    }

    return render(request, 'index.html', context)

def room(request, **kwargs):

    room_id = kwargs.get("id")
    print(room_id)
    room = Room.objects.get(id=room_id)
    print(room)
    context = {
    "room": room,
}
    return render(request, 'room.html', context)


def create_room(request):
    if request.method == 'POST':
        print(request.COOKIES.get('csrf_token'))
        name = request.POST.get('name')
        text = request.POST.get('text')
        room = Room(name=name, text=text)
        room.save()
        return redirect('home')


    return render(request, 'create_room.html')
