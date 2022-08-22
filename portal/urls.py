from django.urls import path, include
from . import views
from .import AdminViews
urlpatterns = [
    path('',views.loginPage,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('admin_home',AdminViews.admin_home,name='admin_home')
]