"""medico_experts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from doctor_app import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('patient_home/',views.patient_home,name="patient_home"),
    path('doctor_profile/',views.doctor_profile,name="doctor_profile"),
    path('viewdoctor_profile/',views.viewdoctor_profile,name="viewdoctor_profile"),
    path('viewdoc_profile/',views.patientviewdoc_profile,name="viewdoc_profile"),
    path('viewpatient_profile/',views.viewpatient_profile,name="viewpatient_profile"),
    path('patient_profile/',views.patient_profile,name="patient_profile"),
    path('',views.loginpage,name="loginpage"),
    path('registration/',views.registration,name="registration"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('send_otp/',views.send_otp,name="send_otp"),
    path('reset_password/',views.reset_password,name="reset_password"),
    path('appointment/',views.appointment,name="appointment"),
    path('doctor_schedule/',views.doctor_schedule,name="doctor_schedule"),
    path('all_patients/',views.all_patients,name="all_patients"),
    path('add_patients/',views.add_patients,name="add_patients"),
    path('invoice/',views.invoice,name="invoice"),
    path('update_docprofile/',views.update_docprofile,name="update_docprofile"),
    path('all_doctor/',views.all_doctor,name="all_doctor"),
    path('patient_all_doctor/',views.patient_all_doctor,name="patient_all_doctor"),
    path('all_payment/',views.all_payment,name="all_payment"),
    path('edit_patientprofile/',views.edit_patientprofile,name="edit_patientprofile"),
    path('update_patientprofile/',views.update_patientprofile,name="update_patientprofile"),
    path('mark_availability/',views.mark_availability,name="mark_availability"),
    path('store_all_availabilities/',views.store_all_availabilities,name="store_all_availabilities"),
]
