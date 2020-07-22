from django.shortcuts import render
from .models import *
from random import *
from datetime import datetime, timedelta, date

# Create your views here.
def index(request):
    return render(request,'doctor_app/doctor-panel/index.html')

def patient_home(request):
    email=request.session['email']
    uid = User.objects.filter(email=email)
    print('---------------------------',uid)
    print('--------------------',email)
    if uid[0]:   
        pid=Patient.objects.get(user_id=uid[0])
        print('------------------->',pid)
    return render(request,'doctor_app/patient-panel/index.html',{'pid':pid})

def doctor_profile(request):
    email=request.session['email']
    uid = User.objects.filter(email=email)
    print('---------------------------',uid)
    print('--------------------',email)
    if uid[0]:   
        did=Doctor.objects.get(user_id=uid[0])
        print('------------------->',did)
        return render(request,'doctor_app/doctor-panel/profile.html',{'did':did})

def viewdoctor_profile(request):
    return render(request,'doctor_app/doctor-panel/ViewProfile.html')

def patientviewdoc_profile(request):
    return render(request,'doctor_app/patient-panel/ViewDoctorProfile.html')

def viewpatient_profile(request):
    return render(request,'doctor_app/doctor-panel/patients-profile.html')

def patient_profile(request):
    email=request.session['email']
    uid = User.objects.filter(email=email)
    print('---------------------------',uid)
    print('--------------------',email)
    if uid[0]:   
        pid=Patient.objects.get(user_id=uid[0])
        print('------------------->',pid)
    return render(request,'doctor_app/patient-panel/patients-profile.html',{'pid':pid})

def loginpage(request):
    return render(request,'doctor_app/loginpage.html')

def registration(request):
    return render(request,'doctor_app/register.html')

def appointment(request):
    email=request.session['email']
    uid = User.objects.filter(email=email)
    print('---------------------------',uid)
    print('--------------------',email)
    if uid[0]:   
        pid=Patient.objects.get(user_id=uid[0])
        print('------------------->',pid)
    return render(request,'doctor_app/patient-panel/book-appointment.html',{'pid':pid})

def doctor_schedule(request):
    return render(request,'doctor_app/doctor-panel/events.html')

def all_doctor(request):
    email=request.session['email']
    uid = User.objects.filter(email=email)
    print('---------------------------',uid)
    print('--------------------',email)
    if uid[0]:   
        did=Doctor.objects.get(user_id=uid[0])
        print('------------------->',did)
    getall=Doctor.objects.all()
    return render(request,'doctor_app/doctor-panel/doctors.html',{'getall':getall,'did':did})

def patient_all_doctor(request):
    email=request.session['email']
    uid = User.objects.filter(email=email)
    print('---------------------------',uid)
    print('--------------------',email)
    if uid[0]:   
        pid=Patient.objects.get(user_id=uid[0])
        print('------------------->',pid)
    getall=Doctor.objects.all()
    return render(request,'doctor_app/patient-panel/doctors.html',{'getall':getall,'pid':pid})

def all_patients(request):
    email=request.session['email']
    uid = User.objects.filter(email=email)
    print('---------------------------',uid)
    print('--------------------',email)
    if uid[0]:   
        did=Doctor.objects.get(user_id=uid[0])
        print('------------------->',did)
    getall=Patient.objects.all()
    return render(request,'doctor_app/doctor-panel/all-patients.html',{'getall':getall,'did':did})

def add_patients(request):
    return render(request,'doctor_app/doctor-panel/add-patients.html')

def invoice(request):
    return render(request,'doctor_app/doctor-panel/invoice.html')

def all_payment(request):
    return render(request,'doctor_app/doctor-panel/all-payment.html')

def edit_patientprofile(request):
    email=request.session['email']
    uid = User.objects.filter(email=email)
    print('---------------------------',uid)
    print('--------------------',email)
    if uid[0]:   
        pid=Patient.objects.get(user_id=uid[0])
        print('------------------->',pid)
    return render(request,'doctor_app/patient-panel/edit_patientprofile.html',{'pid':pid})

def login(request):
    if request.POST['role'] == 'doctor':
        email = request.POST['email']
        password = request.POST['password']
        uid = User.objects.filter(email=email)
        print(uid)
        if uid[0]:
            if uid[0].password == password and uid[0].role == 'doctor':
                did=Doctor.objects.get(user_id=uid[0])
                doctor = Doctor.objects.filter(user_id=uid[0])
                request.session['email'] = uid[0].email
                request.session['firstname'] = doctor[0].firstname
                request.session['lastname'] = doctor[0].lastname
                request.session['profilepic']=doctor[0].profilepic.url
                request.session['role'] = uid[0].role
                request.session['id'] = uid[0].id

                print("------------------------------>",did.firstname)
                #request.session['profile_pic']=doctor[0].profile_pic
                #print("----------> Profile pic-->", doctor[0].profile_pic.url)
                return render(request,'doctor_app/doctor-panel/index.html',{'did':did})
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "doctor_app/loginpage.html", {'message': message})
        else:
            message = "user doesn't exist"
            return render(request, "doctor_app/loginpage.html", {'message': message})
    else:
        email = request.POST['email']
        password = request.POST['password']
        uid = User.objects.filter(email=email)
        print('---------------------patient--uid',uid)
        if uid[0]:
            if uid[0].password == password and uid[0].role == 'patient':
                pid=Patient.objects.get(user_id=uid[0])
                patient = Patient.objects.filter(user_id=uid[0])
                request.session['email'] = uid[0].email
                request.session['firstname'] = patient[0].firstname
                request.session['lastname'] = patient[0].lastname
                request.session['profilepic']=patient[0].profilepic.url
                request.session['role'] = uid[0].role
                request.session['id'] = uid[0].id
                print('----------------------------------->',pid.firstname)
                print('----------------------------------->',email)
                return render(request,'doctor_app/patient-panel/index.html',{'pid':pid})
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request, "doctor_app/loginpage.html", {'message': message})


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
            print("-------------> role",role)
            print("--------------->",email)
            print("--------------->",firstname)
            print("--------------->",lastname)
            print("--------------->",password)

            uid = User.objects.create(email=email,password=password,role=role)
            d_id=Doctor.objects.create(user_id=uid,firstname=firstname,lastname=lastname)
            msg="Registration successfully"
            return render(request,'doctor_app/loginpage.html',{'msg':msg})
        else:
            print("-------------> patient ----------------",role)
            email=request.POST['email']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            password=request.POST['password']
            
            print("--------------->",email)
            print("--------------->",firstname)
            print("--------------->",lastname)
            print("--------------->",password)
         
            uid=User.objects.create(email=email,password=password,role="patient")
            print("--------------------------> patient -> uid",uid)
            p_id=Patient.objects.create(user_id=uid,firstname=firstname,lastname=lastname)
            msg="Registration successfully"
            return render(request,'doctor_app/loginpage.html',{'msg':msg})
    except:
        msg="Field Require"
        return render(request,'doctor_app/registration',{'msg':msg})

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request, "doctor_app/loginpage.html")
    else:
        return render(request,'doctor_app/doctor-panel/index.html')


def forgot_password (request):
    return render(request,'doctor_app/forgot_password.html')

def send_otp (request):
    email=request.POST['email']
    uid=User.objects.get(email=email)
    if uid:
        otp=randint(1111,9999)
        uid.otp=otp
        uid.save()  #update
        subject="OTP Verification"
        #sendmail(subject,"mail_templates",email,{'otp':otp})
        return render(request,"doctor_app/reset_password.html",{'email':email})
    else:
        return render(request,"doctor_app/forgot_password.html")

def reset_password(request):
    email=request.POST['email']
    otp=request.POST['otp']
    password=request.POST['password']
    uid=User.objects.get(email=email)
    if uid:
        if uid.email==email and str(uid.otp)==otp:
            uid.password=password
            uid.save()
            return render(request,'doctor_app/loginpage.html')
        else:
            msg="invalid otp"
            return render (request,'doctor_app/reset_password.html')
    else:
        return render (request,'doctor_app/reset_password.html')

def update_docprofile(request):
    email=request.POST['email']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    gender=request.POST['gender']
    address=request.POST['address']
    city=request.POST['city']
    residency=request.POST['residency']
    hospital_affiliations=request.POST['hospital_affiliations']
    medical_school=request.POST['medical_school']
    certifications=request.POST['certifications']
    internship=request.POST['internship']
    experience=request.POST['experience']
    speciality=request.POST['speciality']
    about=request.POST['about']
    profilepic=request.FILES['profilepic']
    print("--------------->",email)
    print("--------------->",firstname)
    print("------------------->",profilepic)

    user=User.objects.get(email=email)
    did=Doctor.objects.get(user_id=user)
    if did:
        print("--------------------->",did)
        did.firstname=firstname
        did.lastname=lastname
        did.gender=gender
        did.address=address
        did.city=city
        did.residency=residency
        did.hospital_affiliations=hospital_affiliations
        did.medical_school=medical_school
        did.certifications=certifications
        did.internship=internship
        did.experience=experience
        did.speciality=speciality
        did.about=about
        did.profilepic=profilepic
        did.save()
        user.save()
        print("------------------------> update success ")
        return render(request,'doctor_app/doctor-panel/index.html')
        #return render(request,'doctor_app/dashboard/index.html')
        #return render(request,'doctor_app/doctor/profile.html',{'did':did})
    else:
        return render(request,'doctor_app/doctor-panel/index.html')


def update_patientprofile(request):
    email=request.POST['email']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    gender=request.POST['gender']
    address=request.POST['address']
    occuption=request.POST['occuption']
    phone_no=request.POST['phone_no']
    about=request.POST['about']
    age=request.POST['age']
    profilepic=request.FILES['profilepic']
    print("--------------->",email)
    print("--------------->",firstname)
    print("------------------->",profilepic)

    user=User.objects.get(email=email)
    pid=Patient.objects.get(user_id=user)
    if pid:
        print("--------------------->",pid)
        pid.firstname=firstname
        pid.lastname=lastname
        pid.gender=gender
        pid.address=address
        pid.occuption=occuption
        pid.phone_no=phone_no
        pid.about=about
        pid.age=age
        pid.profilepic=profilepic
        pid.save()
        print('-------------------------> occcuption----', occuption)
        print("------------------------> update success ")
        return render(request,'doctor_app/patient-panel/index.html')
        #return render(request,'doctor_app/dashboard/index.html')
        #return render(request,'doctor_app/doctor/profile.html',{'did':did})
    else:
        return render(request,'doctor_app/patient-panel/index.html')


def mark_availability(request):
    return render(request,'doctor_app/patient-panel/mark_availability.html')

def store_all_availabilities(request):
    if request.session['role'] == 'doctor':
        start_date = datetime.strptime(request.POST['start_date'], "%Y-%m-%d").date()
        end_date = datetime.strptime(request.POST['end_date'], "%Y-%m-%d").date()

        start_time = request.POST['start_time']
        print('this is date', start_date)
        end_time = request.POST['end_time']
        doctor_id = Doctor.objects.get(user_id=request.session['id'])
        
        current_time = date.today()
        
        print(type(current_time))
        print(type(start_date))
        # if start_date > current_time and end_time > current_time:
        
        difference_in_days = end_date - start_date
        for i in range(0, int(difference_in_days.days)+1):
            modified_date = start_date + timedelta(days=i)
            for j in range(int(start_time), int(end_time) + 1):
                availability.objects.create(doctor_id=doctor_id, avail_date=modified_date, start_time=str(j)+':00')
                availability.objects.create(doctor_id=doctor_id, avail_date=modified_date, start_time=str(j)+':30')
        all_availabilities = availability.objects.filter(doctor_id=doctor_id)

        print("--------------->",start_date)
        print("--------------->",start_time)
        print("--------------->",end_date)
        print("--------------->",end_time)
        for all in all_availabilities:
            print("----------->",all)

        return render(request,'doctor_app/patient-panel/mark_availability.html')
        # else:
        #     all_availabilities = availability.objects.filter(doctor_id = doctor_id)
        #     return render(request, "doctorfinder/mark_availability.html", {'all_availabilities': all_availabilities,'error':'Start and end time should be greater than current date'})
    else:
        return render(request,'doctor_app/doctor_panel/index.html')
