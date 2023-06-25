from django.db import models
from datetime import datetime
from django.utils import timezone

class MovieManager(models.Manager):
    def form_validator(self, postData):
        errors = {}
        if len(postData['network']) <3:
            errors['network'] = "Network name should be at least 3 characters"
        if len(postData['title']) <2:
            errors['title'] = "show name should be at least 2 characters"
        form_date = postData['release_date']
        form_datetime = datetime.strptime(form_date, '%Y-%m-%d').date()
        if form_datetime > timezone.now().date():
            errors["release_date"] = "date should be in the past"
        return errors

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField(null=True)
    release_date= models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovieManager()




