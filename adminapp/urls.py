from turtle import home
from django.urls import path
from . import views
from turtle import home
from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('admin_gyminfo',views.admin_gyminfo,name='admin_gyminfo'),
    path('packages',views.packages,name='packages'),
    path('subscription',views.subscription,name='subscription'),
    path('view_subscription',views.view_subscription,name='view_subscription'),
  
    path('add_trainers',views.add_trainers,name='add_trainers'),
   

    path('view_trainers',views.view_trainers,name='view_trainers'),
    path('admin_userlist',views.admin_userlist,name='admin_userlist'),
    path('admin_userpayment',views.admin_userpayment,name='admin_userpayment'),
    path('add_gallery',views.add_gallery,name='add_gallery'),
    path('upload_gallery',views.upload_gallery,name="upload_gallery"),
    path('gallery',views.gallery,name='gallery'),
    path('admin_review',views.admin_review,name='admin_review'),
   
    path('login',views.login,name='login'),

]
