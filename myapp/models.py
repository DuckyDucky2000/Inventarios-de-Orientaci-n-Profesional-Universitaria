from django.db import models
from django.db.models import Sum

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.name

class Test(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()

class Dato(models.Model):
    dato = models.IntegerField()