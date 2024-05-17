from django.shortcuts import render , redirect
from . models import UserReg 
from .forms import Regform , UserForm
from django.contrib import messages

from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'Demo0/home.html')


def loginUser(request):
    page ='login'

    if request.method == 'POST':
        Email=request.POST.get('email').lower()
        Password=request.POST.get('password')

        try:
            Email = UserReg.objects.get('email')
        except:
            messages.error(request,'user doesnt exist')
        user = authenticate(request, email=Email , password=Password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context={'page':page}
    return render(request,'Demo0/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def Reg(request):
    form=Regform()
    if request.method == 'POST':
        form=Regform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            return redirect('login')
        else:
            messages.error(request,'something went wrong!!!')
    context={'form':form}   
    return render(request,'Demo0/login_register.html',context)