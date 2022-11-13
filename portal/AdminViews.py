import email
from django.shortcuts import render, redirect

from django.contrib import messages
from .models import SessionYearModel, CustomUser, Student, Staffs, Courses, Subjects
from django.core.files.storage import FileSystemStorage
from .forms import AddStudentForm, EditStudentForm




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
            username = form.cleaned_data['username']
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
                user = CustomUser.objects.create_user(username=username, password=password ,email=email, first_name = first_name, last_name=last_name, user_type=3)
                user.student.address = address

                session_year_obj = SessionYearModel.objects.get(id=session_year_id)
                user.student.session_year_id = session_year_obj

                user.student.gender = gender
                user.student.profile_pic = profile_pic_url
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


def delete_student(request,student_id):
    student = Student.objects.get(admin=student_id)
    try:
        student.delete()
        messages.success(request,"Student Deleted Successfully")
        return redirect('manage_students')
    except:
        messages.error(request,'Failed to delete the student')
        return redirect('manage_students')



def edit_student(request,student_id):
    request.session['student_id'] = student_id
    student = Student.objects.get(admin=student_id)
    form = EditStudentForm()
    form.fields['email'].initial = student.admin.email
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['address'].initial = student.address
    form.fields['gender'].initial = student.gender
    form.fields['session_year_id'].initial = student.session_year_id.id

    context = {
        "id": student_id,
        "form": form
    }
    return render(request,'admin_templates/edit_student.html',context)

def edit_student_save(request):
    if request.method != "POST":
        messages.error("Invalid Request")
        return redirect('manage_students')
    else:
        student_id = request.session.get('student_id')
        if student_id == None:
            return redirect('/manage_student')
        form = EditStudentForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
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
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()

                student_model = Student.objects.get(admin=student_id)
                student_model.address = address
                session_year_obj = SessionYearModel.objects.get(id=session_year_id)
                student_model.session_year_id = session_year_obj
                student_model.gender = gender
                if profile_pic_url != None:
                    student_model.profile_pic = profile_pic_url
                student_model.save()

                del request.session['student_id']

                messages.success(request,"Student Updated Successfully")
                return redirect('/edit_student/'+student_id)



            except:
                messages.error(request, "Failed to Update Student!")
                return redirect('/edit_student/'+student_id)
        else:
            return redirect('/edit_student/'+student_id)


def add_staff(request):
    return render(request, 'admin_templates/add_staff.html')

def add_staff_save(request):
    if request.method != 'POST':
        messages.error(request,'Invalid Method')
        return redirect('add_staff')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=2)
            user.save()
            messages.success(request,"Staff added successfully")
            return redirect('add_staff')
        except:
            messages.error(request,"Failed to add staff")
            return redirect('add_staff')
    
def manage_staff(request):
    staffs = Staffs.objects.all()

    context = {
        "staffs" : staffs,

    }
    return render(request,'admin_templates/manage_staff.html',context)

def edit_staff(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)

    context = {
        "staff":staff,
        "id": staff_id
    }
    return render(request,'admin_templates/edit_staff.html',context)


def delete_staff(request,staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request,"Staff Deleted Successfully")
        return redirect('manage_staff')
    except:
        messages.error(request,'Failed to delete staff')
        return redirect('manage_staff')


def add_course(request):
    return render(request, "admin_templates/add_course.html")


def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('add_course')
    else:
        course = request.POST.get('course')
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Course Added Successfully!")
            return redirect('add_course')
        except:
            messages.error(request, "Failed to Add Course!")
            return redirect('add_course')

def manage_courses(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'admin_templates/manage_courses.html', context)

def delete_course(request,course_id):
    course = Courses.objects.get(id=course_id)
    course.delete()
    messages.error(request,"Course Deleted Successfully")
    return redirect('manage_courses')
    
def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type='2')
    context = {
        "courses": courses,
        "staffs": staffs
    }
    return render(request, 'admin_templates/add_subject.html', context)


def add_subject_save(request):
    if request.method != "POST":
        messages.error(request, "Method Not Allowed!")
        return redirect('add_subject')
    else:
        subject_name = request.POST.get('subject')

        course_id = request.POST.get('course')
        course = Courses.objects.get(id=course_id)
        
        staff_id = request.POST.get('staff')
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject = Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, "Subject Added Successfully!")
            return redirect('add_subject')
        except:
            messages.error(request, "Failed to Add Subject!")
            return redirect('add_subject')
    
def manage_subjects(request):
    subjects = Subjects.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, 'admin_templates/manage_subjects.html', context)

def delete_subject(request,subject_id):
    subject = Subjects.objects.all()
    subject.delete()
    messages.error(request,'Subject Deleted Successfully')
    return redirect('manage_subjects')