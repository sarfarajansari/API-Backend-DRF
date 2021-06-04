from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClayStudent(models.Model):
    rollNo = models.IntegerField()
    student = models.ForeignKey(User,on_delete=models.CASCADE,related_name="student")

    def __str__(self):
        return self.rollNo

class Lecture(models.Model):
    subject = models.CharField(max_length=30)
    teacher = models.CharField(max_length=40,default="")
    duration = models.IntegerField()
    link = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.subject} with {self.teacher} "  

class LectureTime(models.Model):
    day = models.CharField(max_length=30)
    dayId = models.IntegerField()
    datetime = models.DateTimeField()
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)

    def __str__(self):
        return self.lecture.__str__() + "on " + self.day