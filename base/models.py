from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    username = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.username)
    
class Teacher(models.Model):
    teacher_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    username = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.username)

    
class Course(models.Model):
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField('Student', related_name='courses')
    course = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return str(self.course)