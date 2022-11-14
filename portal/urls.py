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
    path('edit_staff/<staff_id>/', AdminViews.edit_staff, name="edit_staff"),
    path('add_course',AdminViews.add_course,name="add_course"),
    path('add_course_save/',AdminViews.add_course_save,name="add_course_save"),
    path('manage_courses',AdminViews.manage_courses,name="manage_courses"),
    path('delete_course/<course_id>',AdminViews.delete_course,name="delete_course"),
    path('add_subject',AdminViews.add_subject,name="add_subject"),
    path('add_subject_save',AdminViews.add_subject_save,name="add_subject_save"),
    path('manage_subjects',AdminViews.manage_subjects,name='manage_subjects'),
    path('delete_subject/<subject_id>',AdminViews.delete_subject,name="delete_subject"),


# URLS for Staff
    path('staff_home',StaffViews.staff_home,name="staff_home"),
    path('staff_add_result',StaffViews.staff_add_result,name="staff_add_result"),
    path('staff_add_result_save',StaffViews.staff_add_result_save,name="staff_add_result_save"),
    path('get_students/', StaffViews.get_students, name="get_students"),


# URls for Students
    path('student_home',StudentViews.student_home,name="student_home"),
    path('student_view_result',StudentViews.student_view_result,name="student_view_result"),

]