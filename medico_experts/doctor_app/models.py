from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    role = models.CharField(max_length = 10)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

class Doctor(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    speciality = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 10)
    clinic = models.CharField(max_length= 100,blank = True)
    address = models.CharField(max_length= 500, blank= True)
    gender = models.CharField(max_length= 10)
    location = models.CharField(max_length= 30, blank= True)
    residency = models.CharField(max_length = 50)
    about_doc = models.CharField(max_length= 100, blank= True)
    profilepic=models.FileField(upload_to='doctor_app/assets/images/',default='doc_male.png')
    hospital_affiliations=models.CharField(max_length= 100,blank=True)
    medical_school=models.CharField(max_length=100,blank=True)
    certifications= models.CharField(max_length=100,blank=True)
    experience=models.CharField(max_length=100,blank=True)
    internship=models.CharField(max_length=100,blank=True)
    about=models.CharField(max_length=1024,blank=True)

class Patient(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length = 10)
    address = models.CharField(max_length= 500, blank = True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50, blank = True)
    gender = models.CharField(max_length= 10)
    occupation= models.CharField(max_length=100,blank=True)
    phone_no=models.CharField(max_length=10,blank=True)
    about=models.CharField(max_length=1024,blank=True)
    age=models.CharField(max_length=10,blank=True)
    profilepic=models.FileField(upload_to='doctor_app/assets/images/',default='doc_male.png')
    
class availability(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    avail_date = models.DateField()
    start_time = models.CharField(max_length = 100)
    status = models.BooleanField(default= False)
    
class Appointment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete = models.CASCADE)
    availability_id = models.ForeignKey(availability, on_delete = models.CASCADE,default = None)
    appointment_status = models.BooleanField(default = False)
    payment_status = models.BooleanField(default = False)
