from django.shortcuts import render,redirect
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='gym_database')
print('Successfully connected to database')
cur = conn.cursor()

# Create your views here.
def index(request):
    return render(request,'admin/index.html')
def admin_gyminfo(request):
    return render(request,'admin/admin_gyminfo.html')
def subscription(request):
    if request.method == 'POST':
        txt1 = request.POST['txt1']
        txt2 = request.POST['txt2']
        txt3 = request.POST['txt3']
        txt4 = request.POST['txt4']

        print(txt1)
        cur.execute("INSERT INTO `tbl_subscriptions`(`subs_name`,`total_months`,`subs_desc`,`amount`) VALUES('{}','{}','{}','{}')".format(txt1,txt2,txt3,txt4))
        conn.commit()
        return redirect(view_subscription)
    else:
        cur.execute("SELECT * FROM `tbl_subscriptions`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'admin/packages.html' , {'mydata': data})    

def view_subscription(request):
    cur.execute("SELECT * FROM `tbl_subscriptions`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'admin/view_subscription.html',{'mydata': data})
def add_trainers(request):
    if request.method == 'POST':
        txt1 = request.POST['txt1']
        txt2 = request.POST['txt2']
        txt3 = request.POST['txt3']
        txt4 = request.POST['txt4']
        txt5 = request.POST['txt5']
        cur.execute("INSERT INTO `tbl_trainers`(`trainer_id`,`trainer_name`,`phone_no`,`email`,`course_name`) VALUES('{}','{}','{}','{}',{}')".format(txt1,txt2,txt3,txt4,txt5))
        conn.commit()
        return redirect(view_trainers)
    else: 
        cur.execute("SELECT * FROM `tbl_trainers`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'admin/add_trainers.html',{'mydata': data})   


   
def view_trainers(request):
    cur.execute("SELECT * FROM `tbl_trainers`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'admin/view_trainers.html',{'mydata': data})
def packages(request):
    cur.execute("SELECT * FROM `tbl_subscriptions`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'admin/packages.html', {'mydata': data})  
    

    
def admin_userlist(request):
    cur.execute("SELECT * FROM `tbl_memberlist`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'admin/admin_userlist.html',{'mydata': data})   
def admin_userpayment(request):
    cur.execute("SELECT * FROM `tbl_payment`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/admin_userpayment.html', {'mydata': data})  

def add_gallery(request):
    return render(request,'admin/add_gallery.html')  
def upload_gallery(request):
    return render(request,'admin/upload_gallery.html')        
def gallery(request):
    return render(request,'admin/gallery.html')   
def admin_review(request):
    return render(request,'admin/admin_review.html')             
def login(request):
    return render(request,'admin/login.html')                   