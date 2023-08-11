from django.shortcuts import render
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database="gym_database")
print('Successfully connected to database')
cur = conn.cursor()

# Create your views here.
def trainer_intex(request):
    return render(request,'trainer/trainer_intex.html')
def trainer_gym_info(request):
    return render(request,'trainer/trainer_gym_info.html')   
def trainers_appointment(request):
    cur.execute("SELECT * FROM `tbl_appointment`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'trainer/trainers_appointment.html',{'mydata': data})    
def trainer_e_session(request):
    cur.execute("SELECT * FROM `tbl_esession`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'trainer/trainer_e_session.html',{'mydata': data})    
def add_e_session(request):  
    if request.method == 'POST':
        txt1 = request.POST['txt1']
        txt2 = request.POST['txt2']
        txt3 = request.POST['txt3']
        txt4 = request.POST['txt4']
        txt5 = request.POST['txt5']
       
        cur.execute("INSERT INTO `tbl_esession`(`course`,`trainer`,`online_links`,`from_time`,`to_time`) VALUES('{}','{}','{}','{}','{}')".format(txt1,txt2,txt3,txt4,txt5))
        conn.commit()
        return redirect(trainer_e_session)
    else: 
        return render(request,'trainer/trainer_e_session.html', {'mydata': ''})
def trainer_status_appointment(request):
    cur.execute("update 'tbl_appointment_booking' set 'status'='{}' where ''='{}'".format())
    return  redirect(request,'')    
def trainer_cancel_appointment(request):
    return  redirect(request,'')      
def trainer_gallary(request):
    return render(request,'trainer/trainer_gallary.html')        
def trainer_profile(request):
    return render(request,'trainer/trainer_profile.html') 
def trainer_viewprofile(request):
    return render(request,'trainer/trainer_viewprofile.html')    
def reg_log(request):
    return render(request,'trainer/reg_log.html')   
def login(request):
    return render(request,'trainer/login.html')    
def changepassword(request):
    return render(request,'trainer/changepassword.html')   
def forgotpassword(request):
    return render(request,'trainer/forgotpassword.html')    
def trainer_conf_appointment(request):
    return render(request,'trainer/trainer_conf_appointment.html')            

