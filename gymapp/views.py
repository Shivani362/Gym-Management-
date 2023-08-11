from html.entities import name2codepoint
from django.shortcuts import render,redirect
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database="gym_database")
print('Successfully connected to database')
cur = conn.cursor()
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def user_index(request):
    return render(request,'member/user_index.html')


def usergym_info(request):
    cur.execute("SELECT * FROM `tbl_user`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'member/usergym_info.html', {'mydata': data})  
    


def user_packages(request):
    cur.execute("SELECT * FROM `tbl_subscriptions`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))

    return render(request,'member/user_packages.html', {'mydata': data})    
def member_appointment(request):
    cur.execute("SELECT * FROM `tbl_appointment`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'member/member_appointment.html',{'mydata': data})   
def user_esession_schedule(request):
    cur.execute("SELECT * FROM `tbl_esession`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'member/user_esession_schedule.html',{'mydata': data})     
def user_gallery(request):
    return render(request,'member/user_gallery.html') 
def user_profile(request):
    id = 1
    cur.execute("SELECT * FROM tbl_user where user_id = {} ".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request,'member/user_profile.html',{'mydata':data})

def user_review(request):
    cur.execute("SELECT * FROM `tbl_review`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'member/user_review.html',{'mydata': data})   
    
    

def reviewcreate(request):
    return render(request,'member/addreview.html')  

def addreview(request):
    if request.method == 'POST':
        print(request.POST)
        name= request.POST['txt1']
        cur.execute("INSERT INTO `tbl_review`(`review_details`) VALUES('{}')".format(name))
        conn.commit()
        return redirect(reviewcreate)
    else:
        return redirect(reviewcreate)
 
def user_amntpayment(request):
    if request.method == 'POST':
        txt1 = request.POST['txt1']
        txt2 = request.POST['txt2']
        txt3 = request.POST['txt3']
        txt4 = request.POST['txt4']
        cur.execute("INSERT INTO `tbl_payment`(`user_name`,`course`) VALUES('{}','{}')".format(txt1,txt2))
        conn.commit()
        return redirect(user_amntpayment)
    else:
        cur.execute("SELECT * FROM `tbl_payment`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'member/user_amntpayment.html', {'mydata': data})   
def member_appointment_add(request):
    if request.method == 'POST':
        txt1 = request.POST['txt1']
        txt2 = request.POST['txt2']
        txt3 = request.POST['txt3']
        txt4 = request.POST['txt4']
        txt5 = request.POST['txt5']
        cur.execute("INSERT INTO `tbl_appointment_booking`(`name`,`email`,`phone`,`description`,`day`) VALUES('{}','{}','{}','{}','{}')".format(txt1,txt2,txt3,txt4,txt5,))
        conn.commit()
        return redirect(book_appointment_member)
    else:
        return render(request,'member/book_appointment_member.html')   
    
def book_appointment_member(request):
    if request.method == 'POST':
        txt1 = request.POST['txt1']
        txt2 = request.POST['txt2']
        txt3 = request.POST['txt3']
        txt4 = request.POST['txt4']
        txt5 = request.POST['txt5']
        cur.execute("INSERT INTO `tbl_appointment_booking`(`name`,`email`,`phone`,`description`,`day`) VALUES('{}','{}')".format(txt1,txt2,txt3,txt4,txt5,))
        conn.commit()
        return redirect(book_appointment_member)
    else:
        cur.execute("SELECT * FROM `tbl_appointment_booking`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'member/book_appointment_member.html', {'mydata': data})   
  
def update_appointment_member(request):
    return render(request,'member/update_appointment_member.html')   
    
def changepassword(request):
    return render(request,'member/changepassword.html')               
def user_viewprofile(request):
    return render(request,'member/user_viewprofile.html')    
def login(request):
    return render(request,'member/login.html')  
