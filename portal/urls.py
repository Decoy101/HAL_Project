from django.urls import path, include
from portal import StaffViews, StudentViews

from portal.models import Admin
from . import views
from .import AdminViews
urlpatterns = [
    path('',views.loginPage,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('admin_home',AdminViews.admin_home,name='admin_home'),
    path('add_session',AdminViews.add_session,name='add_session'),
    path('add_session_save',AdminViews.add_session_save,name='add_session_save'),
    path('manage_session',AdminViews.manage_session,name="manage_session"),
    path('edit_session/<session_id>/',AdminViews.edit_session,name='edit_session'),
    path('edit_session_save',AdminViews.edit_session_save,name='edit_session_save'),
    path('delete_session/<session_id>/',AdminViews.delete_session,name='delete_session'),
    path('add_student',AdminViews.add_student,name="add_student"),
    path('add_student_save',AdminViews.add_student_save,name='add_student_save'),
    path('manage_students',AdminViews.manage_students,name="manage_students"),
    path('edit_student/<student_id>',AdminViews.edit_student,name="edit_student"),
    path('edit_student_save',AdminViews.edit_student_save,name="edit_student_save"),
    path('delete_student/<student_id>/',AdminViews.delete_student,name="delete_student"),
    path('add_staff',AdminViews.add_staff,name="add_staff"),
    path('add_staff_save',AdminViews.add_staff_save,name="add_staff_save"),
    path('manage_staff',AdminViews.manage_staff,name="manage_staff"),
    path('delete_staff/<staff_id>',AdminViews.delete_staff,name="delete_staff"),

# URLS for Staff
    path('staff_home',StaffViews.staff_home,name="staff_home"),
    


# URls for Students
    path('student_home',StudentViews.student_home,name="student_home"),

]