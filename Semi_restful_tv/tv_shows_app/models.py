from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField(null=True)
    release_date= models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
