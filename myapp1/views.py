from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password2==password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password does not match')
            return redirect('register')
    return render(request,'register.html')