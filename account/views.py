from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
    	messages.info(
    	 request,
    	 'you are already logged in; if you want to log in another account, <a href="/account/logout" class="alert-link" >logout</a> first'
    	)
    	return redirect('index')
    if request.method=='POST':
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(username=username, password=password)
       if user is not None:
            login(request, user)
            messages.success(request, 'Logged in')
            return redirect('index')
       else:
            messages.warning(request, 'Username or password incorrect')
    return render(request,'account/login.html')

def register(request):
    if request.user.is_authenticated:
    	messages.info(
    	 request,
    	 'you are already logged in; if you want to register another account, logout first'
    	 )
    	return redirect('index')
    if request.method=='POST':
        password=request.POST.get('password')
        if password!=request.POST.get('password1'):
            messages.warning(
             request,
             "Password doesn't match"
             )
            return redirect('register')
        username = request.POST['username']
        email = request.POST['email']
        user = authenticate(username=username, password=password)
        if user is None:
            user = User(
            username=username,
            password=make_password(
            	password
            ),
            email=email
            )
            user.save()
            login(request, user)
            messages.success(request, 'Logged in')
            return redirect('index')
        else:
        	messages.warning(
        	  request,
        	  'Username or email already exist'
        	)
        	return redirect('register')
    return render(request, 'account/register.html')

@login_required()
def logout_view(request):
    logout(request)
    messages.info(
      request,
      'sucessfully logged out'
    )
    return redirect('index')

@login_required()
def setting(request):
    return render(request, 'account/setting.html')

@login_required()
def profile(request):
    return render(request, 'account/profile.html')

@login_required()
def profile_edit(request):
	if request.method == 'POST':
		user = User.objects.get(pk=request.user.pk)
		
		avatar = request.POST.get('avatar', None)
		if (avatar is not None) and avatar != '':
			user.avatar = avatar
		user.first_name = request.POST.get('first_name', request.user.first_name)
		user.last_name = request.POST.get('last_name', request.user.last_name)
		user.username = request.POST.get('username', request.user.username)
		user.dob = request.POST.get('dob', request.user.dob)
		user.save()
		messages.success(request, 'Profile updated successfully')
		return redirect('profile')
	return render(request, 'account/profile_edit.html')