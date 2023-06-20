from django.shortcuts import render, redirect, reverse
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        "books" : Book.objects.all()
    }
    return render (request,'index.html',context)

def add_book(request):
    new_book= Book.objects.create(title= request.POST['title'], desc= request.POST['desc'])
    new_book.save()
    return redirect ('/')

def book_info(request, id):
    book=Book.objects.get(id=id)
    context={
    "book": Book.objects.get(id=id),
    "authors" : Author.objects.all().exclude(books=book)
    }
    return render (request, 'Book.html', context)

def author_to_book(request):
    book = Book.objects.get(id=request.POST['book'])
    author_to_be_added = Author.objects.get(id = request.POST['choosen_author'])
    author_to_be_added.books.add(book)
    id = request.POST['book']
    page="books/" +id
    return redirect (page)

def authors(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render (request, "authors.html", context)

def add_author(request):
    new_book= Author.objects.create(first_name= request.POST['first_name'], 
    last_name= request.POST['last_name'],
    notes= request.POST['notes'])
    new_book.save()
    return redirect ('/authors')


def author_info(request, id):
    author = Author.objects.get(id=id)
    context={
    "author": Author.objects.get(id=id),
    "books" : Book.objects.all().exclude(authors=author)
    }
    return render (request, 'Book.html', context)



def author_info(request, id):
    author=Author.objects.get(id=id)
    context={
    "author": Author.objects.get(id=id),
    "books" : Book.objects.all().exclude(authors=author)
    }
    return render (request, 'author_info.html', context)

def book_to_author(request):
    author = Author.objects.get(id=request.POST['author'])
    book_to_be_added = Book.objects.get(id = request.POST['choosen_book'])
    book_to_be_added.authors.add(author)
    id = request.POST['author']
    page="authors/" +id
    return redirect (page)