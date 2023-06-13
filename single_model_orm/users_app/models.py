from django.db import models

# Create your models here.    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email_adress = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# User.objects.create(first_name="Muhammad", last_name="Masharqah", email_adress="masharqah@gmail.com", age=35)
# User.objects.create(first_name="Ali", last_name="Ahmad", email_adress="asdf@gmail.com", age=30)
# User.objects.create(first_name="zaid", last_name="Amr", email_adress="zame@gmail.com", age=55)
