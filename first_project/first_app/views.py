from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("all blogs to be rendered here")

def new(request):
    return HttpResponse ("Here you will find a form to creae new blog")

def create (request):
    return redirect ('/')

def ShowBlogNumber(request, blogNumber):
    content = f'Here we display blog number :  {blogNumber}'
    return HttpResponse(content, content_type='text/plain')

def edit(request,blogNumber ):
    content = f'Placeholder to edit blog number : {blogNumber}'
    return HttpResponse(content, content_type='text/plain')

def destroy(request, blogNumber):
    print ("*"*10+f"I deleted blog Number: {blogNumber}"+"*"*10)
    return redirect('/blogs')

def json(request):
    response = {
        "title": "How to create this",
        "content": " Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }
    return JsonResponse(response)


