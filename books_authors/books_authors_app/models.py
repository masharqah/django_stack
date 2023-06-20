from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author,related_name="books")


    
# book1 = Book.objects.create(title= "C Sharp", desc="Programing language")
# book2 = Book.objects.create(title= "Java", desc="Programing language")
# book3 = Book.objects.create(title= "Python", desc="Programing language")
# book4 = Book.objects.create(title= "PHP", desc="Programing language")
# book5 = Book.objects.create(title= "Ruby", desc="Programing language")

# author1 = Author.objects.create(first_name="Jane",last_name = "Austin")
# author2 = Author.objects.create(first_name="Emily",last_name = "Dikinson")
# author3 = Author.objects.create(first_name="Fyodor",last_name = "Distofsky")
# author4 = Author.objects.create(first_name="William",last_name = "Shakespeare")
# author5 = Author.objects.create(first_name="Lau",last_name = "Tzu")

