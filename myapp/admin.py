from django.contrib import admin

from .models import Contact, Department, Doctors, Appointment, Gallery, Jobtype, Job, Career, Review

# Register your models here.
admin.site.register(Contact)

admin.site.register(Department)

admin.site.register(Doctors)

admin.site.register(Appointment)

admin.site.register(Gallery)

admin.site.register(Jobtype)

admin.site.register(Job)

admin.site.register(Career)

admin.site.register(Review)