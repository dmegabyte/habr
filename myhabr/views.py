from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from main.models import Room
from main.models import Comment

# Create your views here.


def index(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
        'count_rooms': len(rooms),
    }

    return render(request, 'index.html', context)

def room(request, **kwargs):
    if request.method == 'POST':
        text = request.POST.get('text')
        room_id = kwargs.get("id")
        comment = Comment(room_id=room_id, text=text)
        
        comment.save()
        return redirect('view_room', id=room_id)



    room_id = kwargs.get("id")
    print(room_id)
    room = Room.objects.get(id=room_id)
  
    print(room)
    context = {
    "room": room,
  
}
    return render(request, 'room/room.html', context)


def create_room(request):
    if request.method == 'POST':
        print(request.COOKIES.get('csrf_token'))
        name = request.POST.get('name')
        text = request.POST.get('text')
        room = Room(name=name, text=text)
        room.save()
        return redirect('home')


    return render(request, 'room/create_room.html')


def login(request):
    return render(request,"auth/login.html")

def register(request):
    return render(request,"auth/register.html")


def logout(request):
    return redirect("home")
