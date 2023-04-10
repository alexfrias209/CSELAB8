from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    username = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return str(self.username)

class Teacher(models.Model):
    teacher_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    username = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.username)

class Course(models.Model):
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    course = models.CharField(max_length=100)
    students = models.ManyToManyField('Student', related_name='courses')
    schedule = models.CharField(max_length=100, blank=True, null=True)
    capacity = models.IntegerField()

    def __str__(self):
        return str(self.course)
    
    def student_ratio(self):
        num_students = self.students.count()
        return f"{num_students}/{self.capacity}"
    
    def full(self):
        num_students = self.students.count()
        if num_students >= self.capacity:
            return True

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} enrolled in {self.course} - grade {self.grade}"
