from django.shortcuts import render, redirect
from django.http import HttpResponse

def student_home(request):
    return render(request,'student_templates/student_home.html')