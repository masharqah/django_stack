from django.shortcuts import render, redirect
from .models import Dojos, Ninjas

# Create your views here.
def index(request):
    context= {
        "dojos" : Dojos.objects.all() ,
        "ninjas" : Ninjas.objects.all()
    }
    return render (request, 'index.html',context)

def add_entries(request):
    if request.POST['which_form'] == "add_dojo":
        new_dojo=Dojos.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
        new_dojo.save()
    elif request.POST['which_form'] == "add_ninja":
        new_ninja=Ninjas.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo_id=request.POST['dojo'])
        new_ninja.save()
    
    return redirect('/')
    
def del_dojo(request):
    if request.POST['dojo_name']:
        dojo_to_be_deleted= Dojos.objects.get(id =request.POST['dojo_name'])
        dojo_to_be_deleted.delete()
    return redirect ('/')

