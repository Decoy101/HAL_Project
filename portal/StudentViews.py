from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal.models import Student, StudentResult

def student_home(request):
    return render(request,'student_templates/student_home.html')

def student_view_result(request):
    student = Student.objects.get(admin=request.user.id)
    student_result = StudentResult.objects.filter(student_id=student.id)
    context = {
        "student_result": student_result,
    }
    return render(request, "student_templates/view_result.html", context)