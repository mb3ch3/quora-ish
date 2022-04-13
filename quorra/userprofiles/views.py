from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegistration

# Create your views here.
def home(request):
    return render(request,'userprofiles/base.html')

def userRegistration(request):
    form = UserRegistration()
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.info(request,username+'your  account is created, login to continue')
            return redirect('userprofiles:login')

    context = {'form':form}
    return render(request,'userprofiles/register.html',context)

def userLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('quorra_app:home')
        else:
            messages.info(request,'username or password is incorrect')

    return render(request,'userprofiles/login.html')
