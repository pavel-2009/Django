from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course


# Create your views here.


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'single_course.html', {'course': course})

def buy_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'buy_course.html', {'course': course})

