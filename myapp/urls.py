"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from . import views

urlpatterns = [
    path('adminhome/',views.admin_home,name='adminhome'),
    path('admincontact/',views.admin_contactview,name='admincontact'),
    path('admindepartment/',views.admin_department_us,name='admindepartment'),
    path('admindoctors/',views.admin_doctors_us,name='admindoctors'),
    path('admindoctorsdisplay/',views.admin_doctorsview,name='admindoctorsdisplay'),
    path('admindelete/<int:id>',views.admin_delete_us,name='admindelete'),
    path('adminedit/<int:id>',views.admin_edit,name='adminedit'),
    path('adminappointment/',views.admin_appointment_us,name='adminappointment'),
    path('admingallery/',views.admin_gallery_view,name='admingallery'),
    path('adminjob/',views.admin_job,name='adminjob'),
    path('adminapplication/',views.application_view,name='adminapplication'),
    path('',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('about/',views.about_us,name='about'),
    path('news/',views.news_page,name='news'),
    path('appointment/',views.appointment_us,name='appointment'),
    path('contact/', views.contact_us, name='contact'),
    path('department/', views.department_view, name='department'),
    path('doctorsviews/',views.doctors_views,name='doctorsviews'),
    path('doctorsprofile/<int:id>',views.doctors_profile_us,name='doctorsprofile'),
    path('gallery/',views.gallery_us,name='gallery'),
    path('job/',views.job_page_us,name='job'),
    path('jobview/<int:id>',views.job_view_us,name='jobview'),
    path('careeradd/',views.career_add,name='careeradd'),
]
