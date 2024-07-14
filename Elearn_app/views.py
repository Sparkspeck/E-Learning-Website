from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import *
from django.contrib.auth import authenticate, login as auth_login,logout

def index(request):
    my_courses = MyCourse.objects.filter(user=request.user.id)
    return render(request, 'index.html', {'my_courses': my_courses})    
   
def logout_view(request):
    logout(request)
    
    return render(request,'index.html')
    
def indexc(request):
    logout(request)
    
    return render(request, 'indexc.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            error='invaild username or password'
            return render(request,'login.html',{'error':error})
            
        
        

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            error='password not match'
            
            return render(request,'signup.html',{'error':error})
                    
        # Check if user with the given email already exists
        if User.objects.filter(username=email).exists():
            return HttpResponse('User with this email already exists.')
        
        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        print(f"User {email} created successfully.")
        return redirect('login')

    return render(request, 'signup.html')



def courses_view(request):
    my_courses = MyCourse.objects.filter(user=request.user.id)
        
    course_new=Course.objects.all()
  
    return render (request,'courses.html',{'courses':course_new,'my_courses': my_courses})
@login_required
def enroll_view(request,course_id):
    
    course=get_object_or_404(Course,id=course_id)
    MyCourse.objects.create(user=request.user,course=course)
    return redirect('courses')


def course1(request):
  
    if request.method=='POST':
        name=request.POST.get('fe-name')
        review=request.POST.get('fe-review')
        condent=request.POST.get('fe-condent')
        c1=feedback(fe_name=name,fe_review=review,fe_condent=condent)
        c1.save()
        return redirect('course1')
    
    feedbackdel=feedback.objects.all()
    return render (request,'course1.html',{'feedbackdel':feedbackdel})
    






def course2(request):


  
    if request.method=='POST':
        name=request.POST.get('fe-name')
        review=request.POST.get('fe-review')
        condent=request.POST.get('fe-condent')
        c1=feedback(fe_name=name,fe_review=review,fe_condent=condent)
        c1.save()
        return redirect('course2')
    
    feedbackdel=feedback.objects.all()
    return render (request,'course2.html',{'feedbackdel':feedbackdel})

#def course3(request):

def course3(request):
    
    if request.method=='POST':
        name=request.POST.get('fe-name')
        review=request.POST.get('fe-review')
        condent=request.POST.get('fe-condent')
        c1=feedback(fe_name=name,fe_review=review,fe_condent=condent)
        c1.save()
        return redirect('course3')
    
    feedbackdel=feedback.objects.all()
    return render (request,'course3.html',{'feedbackdel':feedbackdel})

#def course3(request):
def about(request):

    return render (request,'about.html')
def pages(request):
    return render (request,'pages.html')
def quiz(request):
    return render (request,'quiz.html')
def quiz_html(request):
    return render (request,'quiz1.html')
def quiz_css(request):
    return render (request,'quiz2.html')
def quiz_js(request):
    return render (request,'quiz3.html')
def quiz_py(request):
    return render (request,'quiz4.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Validate the form data (optional, depending on your requirements)

        # Send email
        send_mail(
            subject,
            f'Name: {name}\nEmail: {email}\n\n{message}',
            settings.DEFAULT_FROM_EMAIL,  # Sender's email (from settings)
            ['soundargcd6@gmail.com'],  # Recipient's email
            fail_silently=False,
        )

        # Optionally, you can redirect to a success page after sending the email
        return HttpResponseRedirect(reverse('contact'))  # Redirect to the same page (GET request)

    return render(request, 'contact.html')
