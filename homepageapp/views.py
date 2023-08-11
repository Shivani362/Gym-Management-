from django.shortcuts import render,redirect

from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database="gym_database")
print('Successfully connected to database')
cur = conn.cursor()


# Create your views here.
def index(request):
    return render(request,'homepage/index.html')
  
def regi(request):
    return render(request,'homepage/regi.html')            

def login(request):
    return render(request,'member/login.html')  


def login(request):
    if request.method == 'POST':
        print(request.POST)
        email_id = request.POST['email']
        password = request.POST['password']
        cur.execute("select * from `tbl_user` where `email_id` = '{}' and `password` = '{}' ".format(email_id,password))
        data = cur.fetchone()
        if data is not None:
            if len(data) > 0:
                #Fetch Data (ID and Email )
                user_id = data[0]
                full_name = data[2]
                email_id = data[6]
                print(user_id)
                print(email_id)
                #Create Session Variable and Store UserID and UserEmail
                request.session['user_id'] = user_id
                request.session['full_name'] = full_name
                request.session['email_id'] = email_id
                #Pass Message to Html Page
                #Create Cookie Variable and Store UserID and UserEmail redirect on Homepage
                response = redirect(homeview)
                response.set_cookie('user_id', user_id)
                response.set_cookie('full_name', full_name)
                response.set_cookie('email_id', email_id)
                return response
            else:
                messages.info(request, 'Details Not Found')
                return render(request, 'homepage/login.html') 
        messages.info(request, 'Login Failed')
        return render(request,'member/login.html')  
    else:
        return render(request,'member/login.html')  


def loginview(request):
    return render(request,'homepage/login.html')

def userlogin(request):
    if request.method == 'POST':
        print(request.POST)
        email_id = request.POST['email']
        password = request.POST['password']
        cur.execute("select * from `tbl_user` where `email_id` = '{}' and `password` = '{}' ".format(email_id,password))
        data = cur.fetchone()
        if data is not None:
            if len(data) > 0:
                #Fetch Data (ID and Email )
                user_id = data[0]
                full_name = data[2]
                email_id = data[6]
                print(user_id)
                print(email_id)
                #Create Session Variable and Store UserID and UserEmail
                request.session['user_id'] = user_id
                request.session['full_name'] = full_name
                request.session['email_id'] = email_id
                #Pass Message to Html Page
                #Create Cookie Variable and Store UserID and UserEmail redirect on Homepage
                response = redirect(homeview)
                response.set_cookie('user_id', user_id)
                response.set_cookie('full_name', full_name)
                response.set_cookie('email_id', email_id)
                return response
            else:
                messages.info(request, 'Details Not Found')
                return render(request, 'homepage/login.html') 
        messages.info(request, 'Login Failed')
        return render(request, 'homepage/login.html')
    else:
        return render(request, 'homepage/login.html')   



def homeview(request):
    if 'email_id' in request.COOKIES and request.session.has_key('email_id'):
        email_id = request.session['email_id']
        email_id = request.COOKIES['email_id']
        print("Session is  " + email_id)
        print("Cookie is  " + email_id)
        return render(request, 'member/home.html')
    else:
        return redirect(loginview)            
def changepassword(request):
    return  render(request,'member/changepassword.html')

def changepassword(request):
    if request.method == 'POST':
        if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
            print(request.POST)
            user_id = request.session['user_id']
            opass = request.POST['opass']
            npass = request.POST['npass']
            cpass = request.POST['cpass']
            cur.execute("select * from `tbl_user` where `user_id` = '{}'".format(user_id))
            db_data = cur.fetchone()
            if db_data is not None:
                if len(db_data) > 0:
                    #Fetch Data
                    oldpassword = db_data[7]
                    if opass == oldpassword:
                        if npass == cpass:
                            cur.execute("update  `tbl_user` set `password` = {} where `user_id` = {}".format(npass,user_id))
                            conn.commit()
                            messages.success(request, 'Password Changed')
                            return render(request, 'member/changepassword.html')
                        else:
                            messages.success(request, 'New and Confirm Password not Match')
                            return render(request, 'member/changepassword.html')
                    else:
                        messages.success(request, 'Old Password not match')
                        return render(request, 'member/changepassword.html')
                else:
                    messages.success(request, 'record not found ')
                    redirect(loginview) 
            else: 
                messages.success(request, 'Error ')
                redirect(loginview) 
        else:
            return redirect(loginview)
    else:
        return render(request, 'member/changepassword.html')
def forgotpass(request):
    if request.method == 'POST':
        print(request.POST)
        email_id = request.POST['txt1']
        cur.execute("select * from `tbl_user` where `email_id` = '{}' ".format(email_id))
        db_data = cur.fetchone()
            
        if db_data is not None:
            if len(db_data) > 0:
                #Fetch Data
                user_id = db_data[5]
                password = db_data[7]
                print(user_id)
                print(password)
                #Mail Send Code
                subject = 'Forgot Password'
                message = ' Your Password is  ' + password
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email_id,]
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, 'Password Sent on your Email ID')
                return redirect(loginview)
            else:
                messages.success(request, 'Wrong Email Details')
                return render(request, 'homepage/forgetpass.html') 
        messages.success(request, 'Wrong Email Details')
        return render(request, 'homepage/forgetpass.html')
    else:
            return render(request, 'homepage/forgetpass.html')    



def userlogin(request):
    if request.method == 'POST':
        print(request.POST)
        email_id = request.POST['email']
        password = request.POST['password']
        cur.execute("select * from `tbl_user` where `email_id` = '{}' and `password` = '{}' ".format(email_id,password))
        data = cur.fetchone()
        if data is not None:
            if len(data) > 0:
                #Fetch Data (ID and Email )
                user_id = data[0]
                full_name = data[2]
                email_id = data[6]
                print(user_id)
                print(email_id)
                #Create Session Variable and Store UserID and UserEmail
                request.session['user_id'] = user_id
                request.session['full_name'] = full_name
                request.session['email_id'] = email_id
                #Pass Message to Html Page
                #Create Cookie Variable and Store UserID and UserEmail redirect on Homepage
                response = redirect(homeview)
                response.set_cookie('user_id', user_id)
                response.set_cookie('full_name', full_name)
                response.set_cookie('email_id', email_id)
                return response
            else:
                messages.info(request, 'Details Not Found')
                return render(request, 'homepage/login.html') 
        messages.info(request, 'Login Failed')
        return render(request, 'homepage/login.html')
    else:
        return render(request, 'homepage/login.html')         

 


        
   