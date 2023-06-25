from django.shortcuts import render, redirect
from .models import Course , Description, Comment
from django.contrib import messages

# Create your views here.
def index (request):
    context = {
        "courses" : Course.objects.all()
    }
    return render (request, 'index.html', context)

def add_course(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    description = Description.objects.create(
        content=request.POST['description']
        )
    description.save()
    added_course = Course.objects.create(
        name = request.POST['name'],
        description= description
    )
    added_course.save()
    return redirect('/')

def comments(request, id):
    course=Course.objects.get(id=id)
    context = {
        "course" : course
    }
    return render(request, 'comments.html', context)

def add_comment(request, id):
    course = Course.objects.get(id=id)
    added_comment=Comment.objects.create(
        content = request.POST['content'],
        course= course
    )
    added_comment.save()
    return redirect (f'/comments/{id}')

def remove_course(request, id):
    course_to_be_deleted= Course.objects.get(id=id)
    course_to_be_deleted.delete()
    return redirect('/')

