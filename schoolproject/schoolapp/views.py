from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . models import Department,Course



# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    form=CreateUserForm()
    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('school:login')

    context={'form':form}
    return render(request,'register.html',context)


def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('username')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('school:form')
        else:
            messages.info(request,'Username OR Password is incorrect')
            return render(request,'login.html')
    return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect('school:login')

def form(request):
    return render(request,'form.html')

def getdata(request):
    department = Department.objects.all()
    courses = Course.objects.all()

    return render(request,'regform.html',{'department':department,'courses':courses})

def confirm(request):
    return render(request,'confirm.html')