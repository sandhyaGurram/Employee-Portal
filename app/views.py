from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    emp=Employee.objects.all()
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'home.html',{'emp':emp,'form':form})

def register_user(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            return HttpResponse("Passwords not same")
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('login')
    return render(request,'register.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        n_user=authenticate(username=username,password=password)
        if n_user is not None:
            login(request,n_user)
            return redirect('home')
        
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def add_emp(request):
    form1=EmployeeForm()
    if request.method=='POST':
        form1=EmployeeForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')
    return render(request,'add_emp.html',{'form1':form1})

def view_emp(request,pk):
    if request.user.is_authenticated:
        view=Employee.objects.get(id=pk)

        return render(request,'view_emp.html',{'view':view})
    
def update_emp(request,pk):
    update=Employee.objects.get(id=pk)
    form=EmployeeForm(instance=update)
    if request.method=='POST':
        form=EmployeeForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('view_emp',pk=update.id)
    return render(request,'update_emp.html',{'form':form,'update':update})

def delete_emp(request,pk):
    if request.user.is_authenticated:
        del_emp=Employee.objects.get(id=pk)
        del_emp.delete()
        return redirect('home')
    else:
        return redirect('home')