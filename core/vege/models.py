from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe/")
    receipe_view_count = models.IntegerField(default=0)



class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.deparartment
    
    class Meta:
        ordering=['department']


class StudentID(models.Model):
    student_id = models.IntegerField()

    def __str__(self) -> str:
        return self.student_id

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.student_name
    
    # class Meta:
        # ordering=['student_name']
        # verbose="student"  #which name of db table to save

