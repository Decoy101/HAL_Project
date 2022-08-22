from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('logout_user/',views.logout_user,name='logout_user')
]