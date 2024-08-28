from django.shortcuts import render, redirect

from .forms import ContactForm, DepartmentForm, DoctorsForm, AppointmentForm, GalleryForm, JobForm, CareerForm, \
    ReviewForm
from .models import Contact, Department, Doctors, Appointment, Gallery, Job, Career, Review


# Create your views here.
def admin_home(request):
    return render(request,'admin_home.html')


def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def about_us(request):
    return render(request, 'about.html')


def news_page(request):
    return render(request, 'news.html')

def appointment_us(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = AppointmentForm()
    return render(request,'appointment.html',{'form':form})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})

def department_view(request):
    query = request.GET.get('query')
    if query:
        department_data = Department.objects.filter(Title__icontains=query) | Department.objects.filter(
           Description__icontains=query)
        if department_data:
            return render(request, 'department_view.html', {'department_data': department_data})
        else:
            print("Error.html")
    else:
        result_data = Department.objects.all
    return render(request, 'department_view.html',{'result_data':result_data})




def admin_contactview(request):
    contact_data = Contact.objects.all
    return render(request,'admin_contact_view.html',{'contact_data':contact_data})

def admin_department_us(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
        else:
            print(form.errors)
    else:
        form = DepartmentForm()
    return render(request,'admin_department.html',{'form':form})


def admin_doctors_us(request):
    if request.method == 'POST':
        form = DoctorsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admindoctorsdisplay')
        else:
            print(form.errors)
    else:
        form = DoctorsForm()
    return render(request,'admin_doctors.html',{'form':form})



def admin_doctorsview(request):
    doctors = Doctors.objects.all
    return render(request,'admin_doctors_dispaly.html',{'doctors':doctors})

def admin_delete_us(request,id):
    data = Doctors.objects.get(id=id)
    data.delete()
    return redirect('admindoctorsdisplay'),


def admin_edit(request,id):
    data = Doctors.objects.get(id=id)
    if request.method == 'POST':
        form = DoctorsForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('admindoctorsdisplay')
        else:
            print(form.errors)
    else:
        form = DoctorsForm()
    return render(request,'admin_edit.html',{'data':data,'form':form})


def doctors_views(request):
    query = request.GET.get('query')
    if query:
        doctors = Doctors.objects.filter(doc_name__icontains=query)| Doctors.objects.filter(doc_dep__Title__icontains=query)
        if doctors:
            return render(request, 'team.html', {'doctors': doctors})
        else:
            print("Error.html")
    else:
        results = Doctors.objects.all
    return render(request, 'team.html', {'results': results})


def doctors_profile_us(request,id):
    data = Doctors.objects.get(id=id)
    review = Review.objects.filter(docname=data).order_by('-created_at')

    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.instance.docname = data
            form.save()
            return redirect('doctorsprofile',id=data.id)
        else:
            print(form.errors)
    else:
        form = ReviewForm()
    context={'data':data,'form':form,'review':review}
    return render(request,'doctors_prof.html',context)

def admin_appointment_us(request):
    appointment_data = Appointment.objects.all
    return render(request,'admin_appointment.html',{'appointment_data':appointment_data})



def admin_gallery_view(request):
        if request.method == 'POST':
            form = GalleryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('adminhome')
            else:
                print(form.errors)
        else:
            form = GalleryForm()
        return render(request, 'admin_gallery.html', {'form':form})

def gallery_us(request):
    gallery_data = Gallery.objects.all
    return render(request,'gallery.html',{'gallery_data':gallery_data})


def admin_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
        else:
            print(form.errors)
    else:
        form = JobForm()
    return render(request, 'admin_job.html', {'form': form})


def job_page_us(request):
    job_data = Job.objects.all
    return render(request,'job_page.html',{'job_data':job_data})

def job_view_us(request,id):
    data = Job.objects.get(id=id)
    return render(request,'job_view.html',{'data':data})


def career_add(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job')
        else:
            print(form.errors)
    else:
        form = CareerForm()
    return render(request, 'career_apply.html', {'form': form})

def application_view(request):
    application_data = Career.objects.all
    return render(request,'admin_application.html',{'application_data':application_data})