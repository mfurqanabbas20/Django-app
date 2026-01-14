from django.db import models

# Create your models here.

class Student(models.Model):
    # id = model.AutoField()
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length = 8)
    grade = models.IntegerField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()

# models = model maanger