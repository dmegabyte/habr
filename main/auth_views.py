from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from main.models import Room
from main.models import Comment
from django.shortcuts import render, redirect
from main.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

ALLOWED_SYMBOLS = 'abcdefghijklmnopqrstvwxyz0123456789_'

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user == None:
            return render(request,"auth/login.html", {"error": "Нет такого пользователя"})
        login(request, user)
        return redirect("home")
        


    return render(request,"auth/login.html")

def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')
        if password != confirm_password:
            return render(request,"auth/register.html", {"error": "Пароли не совпадают"})
        
        if len(username) < 3 or len(username) > 30:
            return render(request,"auth/register.html", {"error": "Username должен быть от 3 до 30 символов"})
        
        if not all(char in ALLOWED_SYMBOLS for char in username):
            return render(request,"auth/register.html", {"error": "Username может содержать только английские буквы, цифры и _"})
        
            

        try:
            password = make_password(password)
            user = User.objects.create(username=username, password=password)
            user.save()
    
        except Exception as e:
            return render(request,"auth/register.html", {"error": str(e)})

        return redirect("home")
    return render(request,"auth/register.html")


def logout_page(request):
    logout(request)
    return redirect("home")


