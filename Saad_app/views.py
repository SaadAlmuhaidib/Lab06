# Saad_app/views.py

from django.shortcuts import render, redirect
from .models import Student, Course
from django.http import Http404


def students(request):
    if request.method == 'POST':
        # Add logic to handle the form and create new Student
        pass

    all_students = Student.objects.all()
    return render(request, 'Saad_app/students.html', {'students': all_students})


def courses(request):
    if request.method == 'POST':
        # Add logic to handle the form and create new Course
        pass

    all_courses = Course.objects.all()
    return render(request, 'Saad_app/courses.html', {'courses': all_courses})


def details(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student not found")

    if request.method == 'POST':
        # Add logic to handle the form and update Student's courses
        pass

    not_registered_courses = Course.objects.exclude(students=student)
    return render(request, 'Saad_app/details.html', {
        'student': student,
        'notRegisteredCourses': not_registered_courses
    })