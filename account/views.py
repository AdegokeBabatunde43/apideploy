from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']
        
        
        if password== password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User already exists")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "User already exists")
                    return redirect('register')
                else:
                    form = User.objects.create_user(first_name=first_name, last_name=last_name,  email=email, username=username, password=password)
                    form.save()
                    messages.success(request, "User created successfully")
                    return redirect('signin')
        else:
            messages.error(request, "Password do not match")
            return redirect('register')
    return render(request, 'register.html')



def signin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    return render(request, 'signin.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def signout(request):
    logout(request)
    return redirect('signin')
