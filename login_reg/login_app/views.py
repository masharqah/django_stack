from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render (request,'index.html')

def login(request):
    postData=request.POST
    errors = User.objects.login_validator(postData)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        users=User.objects.filter(email=request.POST['email'])
        logged_user=users[0]
        request.session['name']=f"{logged_user.fname} {logged_user.lname}"
        request.session['logged']=True
        return redirect ('/welcome')

def reg(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        User.objects.create (
            fname= request.POST['fname'],
            lname= request.POST['lname'],
            email= request.POST['email'],
            password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            )
    return redirect ('/success')

def success(request):
    return render (request, 'success.html')

def welcome(request):
    context = {
        'name' : request.session['name'],
        'status' : request.session['logged']
    }
    return render (request, 'welcome.html', context)

def logout(request):
    if request.method == 'POST':
        del request.session['name']
        del request.session['logged']
        request.session.flush()
    return redirect ('/')