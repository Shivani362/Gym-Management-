from django.shortcuts import render
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='gym_database')
print('Successfully connected to database')
cur = conn.cursor()

# Create your views here.
def index(request):
    return render(request,'admin/index.html')
def admin_gyminfo(request):
    return render(request,'admin/admin_gyminfo.html')
def subscriptioncreate(request):
    return render(request,'admin/packages.html')    
def addsubscription(request):
    if request.method == 'POST':
        print(request.POST)
        id= request.POST['txt1']
        cur.execute("INSERT INTO 'tbl_review'('review_details') VALUES('{}')".format(name))
        conn.commit()
        return redirect(subscriptioncreate)
    else:
        return redirect(subscriptioncreate)    
def view_subscription(request):
    cur.execute("SELECT * FROM `tbl_subscriptions`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'admin/view_subscription.html',{'mydata': data})

def add_trainers(request):
    return render(request,'admin/add_trainers.html')
       

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
    
def admin_trainers(request):
    cur.execute("SELECT * FROM `tbl_trainers`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'admin/admin_trainers.html',{'mydata': data}) 
    
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