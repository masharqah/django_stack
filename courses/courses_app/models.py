from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def course_validator(self, postData):
        errors = {}
        if len(postData['name']) <5:
            errors['name'] = " Name should be at least 5 characters"
        if len(postData['description']) <15:
            errors['description'] = "Description should be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField('Description', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=CourseManager()

class Description(models.Model):
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete = models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
