from turtle import home
from django.urls import path
from . import views


urlpatterns = [
    path('trainer_intex',views.trainer_intex,name='trainer_intex'),
    path('trainer_gym_info',views.trainer_gym_info,name='trainer_gym_info'),
    path('trainers_appointment',views.trainers_appointment,name='trainers_appointment'),
    path('trainer_conf_appointment',views.trainer_conf_appointment,name='trainer_conf_appointment'),
    path('trainer_e_session',views.trainer_e_session,name='trainer_e_session'),
    path('add_e_session',views.add_e_session,name='add_e_session'),
    path('trainer_gallary',views.trainer_gallary,name='trainer_gallary'),
    path('trainer_profile',views.trainer_profile,name='trainer_profile'),
    path('trainer_viewprofile',views.trainer_viewprofile,name='trainer_viewprofile'),
    path('trainer_status_appointment',views.trainer_status_appointment,name='_status_appointment'),
    path('trainer_cancel_appointment',views.trainer_cancel_appointment,name='trainer_cancel_appointment'),
    path('reg_log',views.reg_log,name='reg_log'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),


]