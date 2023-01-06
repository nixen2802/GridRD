from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import JobSeeker
import random
import re 

def index(request):
	return render(request, 'index.html')

def view_function(request):
    messages.add_message(request, messages.INFO, 'This is an info message')
    messages.add_message(request, messages.ERROR, 'This is an error message')
    return redirect('main:index')

def user_login(request):
		if request.method == 'POST':
			username = request.POST['email']
			password = request.POST['pass']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('main:candidates')
			else:
				messages.success(request, 'Invalid username or password')
				return redirect('main:user_login')
		else:
			return render(request, 'sign-in.html')

def register(request):
	if request.method=='POST':
		if request.POST['name']=="" or request.POST['email']=="" or request.POST['name']=="" or request.POST['phone']=="":
			messages.error(request, "Dont forget to fill out every field with the appropriate information")
			return render(request, 'sign-up.html')
		if not re.fullmatch(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', request.POST['password']):
			messages.error(request, "Please entere a valid password")
			return render(request, 'sign-up.html')
		jobseeker = JobSeeker()
		jobseeker.user_id = random.randint(0, 1000000000)
		jobseeker.email = request.POST['email']
		jobseeker.password = request.POST['password']
		jobseeker.name = request.POST['name']
		jobseeker.phone = request.POST['phone']
		jobseeker.save()
		messages.success(request, 'Successfully Registered')
		return redirect('main:user_login')
	return render(request, 'sign-up.html')

def blog(request):
	return render(request, 'blog-list-1.html')

def companies(request):
	return render(request, 'companies-list-3.html')

def candidates(request):
	return render(request, 'candidates-list-3.html')

def postjob(request):
	return render(request, 'company-dashboard-new-job.html')

def findjobs(request):
	context = {
    'var': 6
    }
	return render(request, 'jobs-list-3.html',context)

