from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def loginuser(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('HomeView')
            else:
                messages.error(request,'Invalid Username or Password')
        else:
                messages.error(request,'Invalid Username or Password')
    else:
        form=AuthenticationForm()
    return render(request,'session/login.html',{'form':form})

def logoutuser(request):
    logout(request)
    messages.success(request,"Successfully Log out")
    return redirect('HomeView')

def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username=User.username
            email=form.cleaned_data.get('email')
            message = 'Welcome to Tuition BD .Please Click confirm to registration'
            send_mail(
                username,
                message,
                'settings.EMAIL_HOST_USER',
                [email],
                fail_silently=False
            )
            return redirect('login')

    else:
        form=SignUpForm()
    return render(request,'session/signup.html',{'form':form})

# 

def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Successfully changed')
            return redirect('HomeView')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'session/change_password.html',{'form':form})