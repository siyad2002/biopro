from django import forms

from .models import Contact, Department, Doctors, Appointment, Gallery, Job, Jobtype, Career, Review


class ContactForm(forms.ModelForm):
    Name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}))
    Subject = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    Message = forms.CharField(max_length=50,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))
    class Meta:
        model = Contact
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    Title = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'title'}))
    Description = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description','rows':5}))

    class Meta:
        model = Department
        fields = '__all__'




class DoctorsForm(forms.ModelForm):
    doc_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Doctors name'}))
    designation = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'details'}))
    age = forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'candidate age'}))
    doc_img = forms.ImageField(label='Photo',widget=forms.FileInput(attrs={'class':'form-control'}))
    exp = forms.IntegerField(label='Experience',widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Candidate experience'}))
    doc_dep = forms.ModelChoiceField(queryset=Department.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    qualification = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'qualifications'}))
    opening_time = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'time'}))
    day = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'days'}))
    place = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'country'}))
    class Meta:
        model = Doctors
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Fullname'}))
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    contact = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),empty_label="Choose your department")
    doctors = forms.ModelChoiceField(queryset=Doctors.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}),empty_label="Choose your doctors")
    booking_datetime = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    class Meta:
        model = Appointment
        fields = '__all__'

class GalleryForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Upload image'}))
    video = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload video'}))
    description = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}))

    class Meta:
        model = Gallery
        fields = '__all__'

class JobForm(forms.ModelForm):
    jobtype = forms.ModelChoiceField(queryset=Jobtype.objects.all(),widget=forms.Select(attrs={'class':'form-control','placeholder':'Job Type'}))
    job_name = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Job Name'}))
    about_role = forms.CharField(max_length=400,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About Role','rows':5}))
    requirements = forms.CharField(max_length=400,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Requirements'}))
    company_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_name'}))
    about_name = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'About Name',}))
    class Meta:
        model = Job
        fields = '__all__'

class CareerForm(forms.ModelForm):
    firstname = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Firstname'}))
    lastname = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    contact = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}))
    apply_for = forms.ModelChoiceField(queryset=Job.objects.all(),widget=forms.Select(attrs={'class': 'form-control',}))
    qualification = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qualifications'}))
    biodata = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Biodata'}))

    class Meta:
        model =Career
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class':'form-control','rows':6}))

    class Meta:
        model = Review
        exclude = ['docname']