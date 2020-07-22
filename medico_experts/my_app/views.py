from django.shortcuts import render
from .models import *
from random import *
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'my_app/index.html')

def loginpage(request):
    return render(request,'my_app/loginpage.html')

def registrationdoctor(request):
    return render(request,'my_app/registrationdoctor.html')

def registrationpatient (request):
    return render(request,'my_app/registrationpatient.html')

def login(request):
    if request.POST['role'] == 'doctor':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)
        if user[0]:
            if user[0].password == password and user[0].role == 'doctor':
                doctor = Doctor.objects.filter(user_id=user[0])
                request.session['email'] = user[0].email
                request.session['firstname'] = doctor[0].firstname
                request.session['lastname'] = doctor[0].lastname
                request.session['role'] = user[0].role
                request.session['id'] = user[0].id

               # request.session['profile_pic']=doctor[0].profile_pic
                #print("----------> Profile pic-->", doctor[0].profile_pic.url)

                return render(request, "doctor_app/dashboard/index.html")
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "my_app/loginpage.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "my_app/loginpage.html", {'message': message})
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email)
        print(user)
        if user[0]:
            if user[0].password == password and user[0].role == 'patient':
                patient = Patient.objects.filter(user_id=user[0])
                request.session['email'] = user[0].email
                request.session['firstname'] = patient[0].firstname
                request.session['lastname'] = patient[0].lastname
                request.session['role'] = user[0].role
                request.session['id'] = user[0].id

               # request.session['profile_pic']=doctor[0].profile_pic
                #print("----------> Profile pic-->", doctor[0].profile_pic.url)

                return render(request, "my_app/index.html")
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "my_app/loginpage.html", {'message': message})


def register(request):
    role=request.POST['role']
    print("-------------> role",role)
    try:
        print("-------------> role",role)
        if role=="doctor":
            email=request.POST['email']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            cnfpassword=request.POST['cnfpassword']
            print("-------------> role",role)
            print("--------------->",email)
            print("--------------->",firstname)
            print("--------------->",lastname)
            print("--------------->",password)
            print("--------------->",cnfpassword)

            uid = User.objects.create(email=email,password=password,role=role)
            #print(answer)
            d_id=Doctor.objects.create(user_id=uid,firstname=firstname,lastname=lastname)
            msg="Registration successfully"
            return render(request,'my_app/loginpage.html',{'msg':msg})
            
            #return render(request,'my_app/registrationdoctor.html',{'msg':msg})
        else:
            print("-------------> patient ----------------",role)
            email=request.POST['email']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            cnfpassword=request.POST['cnfpassword']
            print("--------------->",email)
            print("--------------->",firstname)
            print("--------------->",lastname)
            print("--------------->",password)
            print("--------------->",cnfpassword)
            

            if password==cnfpassword:
                uid=User.objects.create(email=email,password=password,role="patient")
                print("--------------------------> patient -> uid",uid)
                p_id=Patient.objects.create(user_id=uid,firstname=firstname,lastname=lastname)
                msg="Registration successfully"
                return render(request,'my_app/loginpage.html',{'msg':msg})
            else:
                msg="password does not match "
                return render(request,'my_app/registrationpatient.html',{'msg':msg})  
    except:
        msg="Field Require"
        return render(request,'my_app/registrationdoctor',{'msg':msg})


def logout(request):
    if 'email' in request.session:
        del request.session['id']
        del request.session['firstname']
        del request.session['email']
        return render(request,'my_app/index.html')
    else:
        return render(request,'my_app/loginpage.html')


def forgot_password (request):
    return render(request,'my_app/forgot_password.html')

def send_otp (request):
    email=request.POST['email']
    uid=User.objects.get(email=email)
    if uid:
        otp=randint(1111,9999)
        uid.otp=otp
        uid.save()  #update
        subject="OTP Verification"
        #sendmail(subject,"mail_templates",email,{'otp':otp})
        return render(request,"my_app/reset_password.html",{'email':email})
    else:
        return render(request,"my_app/forgot_password.html")

def reset_password(request):
    email=request.POST['email']
    otp=request.POST['otp']
    password=request.POST['password']
    uid=User.objects.get(email=email)
    if uid:
        if uid.email==email and str(uid.otp)==otp:
            uid.password=password
            uid.save()
            return render(request,'my_app/loginpage.html')
        else:
            msg="invalid otp"
            return render (request,'my_app/reset_password.html')
    else:
        return render (request,'my_app/reset_password.html')
