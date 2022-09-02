from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
import json

from .models import CustomUser, Staffs

def staff_home(request):
    return render(request,'staff_templates/staff_home.html')
    