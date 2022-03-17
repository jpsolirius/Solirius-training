from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=15)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='projects/static/img/')
    created_on = models.DateTimeField(auto_now_add=True)
    technologies = models.ManyToManyField('Technology')

