from urllib import request
from django.shortcuts import render,redirect
from . models import Newuser
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        Newuser(username=username,email=email,password=password,gender=gender).save()
        messages.success(request,"The new user"+request.POST['username']+" Registration successful")
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')


def loginpage(request):
    if request.method =="POST":
        try:
            userdetails = Newuser.objects.get(email = request.POST['email'],password = request.POST['password'])
            # print('username',userdetails)
            request.session['email']=userdetails.email
            return redirect('home')
        except Newuser.DoesNotExist as e:
            messages.warning(request,'invalid username or password')
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'home.html')
    return render(request,'home.html')