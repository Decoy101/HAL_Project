from django.shortcuts import render, redirect
from portal.models import CustomUser

def admin_home(request):
    return render(request,'admin_templates/home.html')

