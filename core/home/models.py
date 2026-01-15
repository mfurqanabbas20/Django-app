from django.db import models

# Create your models here.

# Car.objects.create()

# Car.objects.all()

# Car.objects.get(id=1)

# Car.objects.filter(id=1) => []

# first get car then update info and save

# Car.objects.filter(id=1).update(car_name = "Creta")


class Student(models.Model):
    # id = model.AutoField()
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length = 8)
    grade = models.IntegerField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField()

# models = model maanger

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name
