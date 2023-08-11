from turtle import home
from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.index,name='index'),
    path('regi',views.regi,name='regi'),
    path('login',views.login,name='login'),
    path('loginview',views.loginview,name='loginview'),
    path('homeview',views.homeview,name='homeview'),
    path('userlogin',views.login,name='login'),
   
    path('forgotpass',views.forgotpass,name='forgotpass'),
    

]