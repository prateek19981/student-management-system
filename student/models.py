from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    course=models.CharField(max_length=100)
    year=models.IntegerField()
    address=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    photo=models.ImageField(upload_to='student_photos/')




    def get_absolute_url(self):
        return reverse('student_detail',kwargs={'pk':self.pk})



    def __string__(self):
        return self.name


