from django.urls import path, include
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


]