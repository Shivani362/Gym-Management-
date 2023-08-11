from turtle import home
from django.urls import path
from . import views

urlpatterns = [
    path('user_index',views.user_index,name='user_index'),
    path('usergym_info',views.usergym_info,name='usergym_info'),
    path('user_packages',views.user_packages,name='user_packages'),
    path('member_appointment',views.member_appointment,name='member_appointment'),
    path('member_appointment_add',views.member_appointment_add,name='member_appointment_add'),
    path('user_esession_schedule',views.user_esession_schedule,name='user_esession_schedule'),
    path('user_gallery',views.user_gallery,name='user_gallery'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('user_viewprofile',views.user_viewprofile,name='user_viewprofile'),
    path('user_review',views.user_review,name='user_review'),
    path('addreview',views.addreview,name='addreview'),
    path('reviewcreate',views.reviewcreate,name='addreview'),
    path('reviewcreate/inserted/', views.addreview , name='addreview'),
  
    path('user_amntpayment',views.user_amntpayment,name='user_amntpayment'),
    path('book_appointment_member',views.book_appointment_member,name='book_appointment_member'),
    path('update_appointment_member',views.update_appointment_member,name='update_appointment_member'),
    
    path('changepassword',views.changepassword,name='changepassword'),
   
]

