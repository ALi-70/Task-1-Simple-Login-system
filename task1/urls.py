from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('',views.home,name='hm'),
    # Doctor And Patient Sections
    path('dsec',views.doc_sec,name="dsec"),
    path('psec',views.pat_sec,name="psec"),

    #signup pages for doctor and patient
    path('dsup',views.doctor_signup,name='dsup'),
    path('psup',views.patient_signup,name='psup'),
    #signin pages for doctor and patient
    path('dsin',views.doctor_signin,name='dsin'),
    path('psin',views.patient_signin,name='psin'),
    #profile pages for doctor and patient
    path('dpro',views.doctor_profile,name='dpro'),
    path('ppro',views.patient_profile,name='ppro'),

    path('logout',views.logout1, name="lg"),

    ]