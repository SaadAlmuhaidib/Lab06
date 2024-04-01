# Saad_app/models.py

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields you need

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    # Add any other fields you need
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name