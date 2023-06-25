from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Movie
# Create your views here.

def shows(request):
   
    context = {
        "shows" : Movie.objects.all()
    }
    return render (request,'shows.html',context)

def add_show_form(request):
    return render (request, 'add_show_form.html')

def add_show(request):
    # validations for adding form
    errors = Movie.objects.form_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    added_movie = Movie.objects.create (
        title= request.POST['title'],
        network= request.POST['network'],
        release_date =request.POST['release_date']
    )
    added_movie.save()
    return redirect ('/shows')

def show_info(request, id):
    show = Movie.objects.get (id=id)
    context = {
        "show" : show    
    }
    return render (request, 'show_info.html', context)

def delete_show(request, id ):
    show_to_be_deleted= Movie.objects.get(id = id)
    show_to_be_deleted.delete()
    return redirect ('/shows')

def edit_show_form(request, id):
    show = Movie.objects.get(id=id)
    context ={
        "show" : show
    }
    return render (request, 'edit_show_form.html', context)

def edit_show(request, id):
    # validations for editing form
    errors = Movie.objects.form_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/edit/'+id)

    show = Movie.objects.get(id=id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date= request.POST['release_date']
    show.save()
    return redirect ('/shows')