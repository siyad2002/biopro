from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Subject = models.CharField(max_length=10)
    Email = models.EmailField(null=True)
    Message = models.TextField(max_length=100)
    def __str__(self):
        return self.Name


class Department(models.Model):
    Title = models.CharField(max_length=30,null=True)
    Description = models.TextField(max_length=200,null=True)
    def __str__(self):
        return self.Title


class Doctors(models.Model):
    doc_name = models.CharField(max_length=30,null=True)
    doc_dep = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='dep_name')
    designation = models.TextField(null=True)
    age = models.IntegerField(null=True)
    doc_img = models.ImageField(null=True,upload_to='doctors')
    exp = models.IntegerField(null=True)
    qualification = models.CharField(max_length=50,null=True)
    opening_time = models.CharField(max_length=30,null=True)
    day = models.CharField(max_length=30,null=True)
    place = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.doc_name


class Appointment(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30,null=True)
    contact = models.IntegerField(null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='dep')
    doctors = models.ForeignKey(Doctors,on_delete=models.CASCADE,related_name='doctors')
    booking_time = models.DateTimeField(auto_now_add=True)
    booking_datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(null=True,upload_to='image')
    video = models.FileField(null=True,upload_to='video')
    description = models.CharField(max_length=40,null=True)

    def __str__(self):
        return self.description

class Jobtype(models.Model):
    name = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    jobtype = models.ForeignKey(Jobtype,on_delete=models.CASCADE,related_name='job')
    job_name = models.CharField(max_length=400,null=True)
    about_role = models.CharField(max_length=400, null=True)
    requirements = models.CharField(max_length=400, null=True)
    company_name = models.CharField(max_length=40, null=True)
    about_name = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.job_name

class Career(models.Model):
    firstname = models.CharField(max_length=20,null=True)
    lastname = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=10,null=True)
    apply_for = models.ForeignKey(Job,on_delete=models.CASCADE,related_name='apply')
    qualification = models.CharField(max_length=50,null=True)
    biodata = models.FileField(null=True,upload_to='biodata')

    def __str__(self):
        return self.firstname

class Review(models.Model):
    docname = models.ForeignKey(Doctors,on_delete=models.CASCADE,related_name='docname')
    review_text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review_text