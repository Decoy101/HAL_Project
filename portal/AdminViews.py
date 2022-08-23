from django.shortcuts import render, redirect

from django.contrib import messages
from .models import SessionYearModel, CustomUser, Student
from django.core.files.storage import FileSystemStorage
from .forms import AddStudentForm




def admin_home(request):
    return render(request,'admin_templates/home.html')

def add_session(request):
    return render(request,'admin_templates/add_session.html')

def add_session_save(request):
    if request.method != 'POST':
        messages.error(request,'Invalid Method')
        return redirect('add_course')

    else:
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            sessionyear = SessionYearModel(session_start_year = session_start_year, session_end_year = session_end_year)
            sessionyear.save()
            messages.success(request,"Session Year added Successfully!")
            return redirect("add_session")
        except:
            messages.error(request, "Failed to Add Session Year")
            return redirect('add_session')

def manage_session(request):
    session_years = SessionYearModel.objects.all()
    context = {
        'session_years': session_years
    }
    return render(request,'admin_templates/manage_session.html',context)


def edit_session(request,session_id):
    session_year = SessionYearModel.objects.get(id=session_id)
    context = {
        "session_year": session_year
    }
    return render(request,'admin_templates/edit_session.html',context)

def edit_session_save(request):
    if request.method != "POST":
        messages.error(request,"Invalid MEthod!")
        return redirect('manage_session')
    else:
        session_id = request.POST.get('session_id')
        session_start_year = request.POST.get('session_start_year')
        session_end_year = request.POST.get('session_end_year')

        try:
            session_year = SessionYearModel.objects.get(id=session_id)
            session_year.session_start_year = session_start_year
            session_year.session_end_year = session_end_year
            session_year.save()

            messages.success(request, "Success Year Updated Successfully")
            return redirect('/edit_session/'+session_id)
        except:
            messages.error(request,"Failed to Update Session Year")
            return redirect('/edit_session'+session_id)

def delete_session(request,session_id):
    session_year = SessionYearModel.objects.get(id=session_id)
    try:
        session_year.delete()
        messages.success(request,"Successfully deleted the session")
        return redirect('manage_session')
    except:
        messages.error(request,"Failed to delete session")
        return redirect('manage_session')


def add_student(request):
    form = AddStudentForm()
    context = {
        "form":form
    }
    return render(request,'admin_templates/add_student.html',context)

def add_student_save(request):
    if request.method != "POST":
        messages.error(request,"Invalid Method")
        return redirect('add_student')
    else:
        form = AddStudentForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            session_year_id = form.cleaned_data['session_year_id']
            gender = form.cleaned_data['gender']

            if len(request.FILES) != 0:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name,profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                user = CustomUser.objects.create_user(password=password,email=email, first_name = first_name, last_name=last_name, user_type=3)
                user.students.address = address

                session_year_obj = SessionYearModel.objects.get(id=session_year_id)
                user.students.session_year_id = session_year_obj

                user.student.gender = gender
                user.students.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "Student Added Successfully!")
                return redirect('add_student')
            except:
                messages.error(request, "Failed to Add Student!")
                return redirect('add_student')
        else:
            return redirect('add_student')
        

def manage_students(request):
    students = Student.objects.all()
    context = {
        "students":students

    }
    return render(request, 'admin_templates/manage_students.html',context)


