from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todoApp import models
from .models import TODO
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request, "home.html")

def signup(request):
    if request.method=='POST':
        username=request.POST.get('fnm')
        email=request.POST.get('email')
        pass1=request.POST.get('pwd1')
        pass2=request.POST.get('pwd2')

        if pass1!=pass2:
            return HttpResponse("Confirm Passwords do NOT match!!")
        else:
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('user_login')
    
    return render(request, "signup.html")
        

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('fnm')
        pass1=request.POST.get('pwd1')
        
        user=authenticate(request, username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('todopage')
        else:
            return redirect('/user_login')

    return render(request,'login.html')

@login_required(login_url='/login')
def todopage(request):
    if request.method=='POST':
        title=request.POST.get('title')
        # date = request.POST.get('date')
        print('title')
        if title:
            obj=models.TODO(title=title,user=request.user)
            obj.save()
        res=models.TODO.objects.filter(user=request.user).order_by('-date')
        return render(request,'todo.html',{'res':res})
    
    res=models.TODO.objects.filter(user=request.user).order_by('-date')
    return render(request,'todo.html',{'res':res})

@login_required(login_url='/login')
def edit_todo(request,srno):
    if request.method=='POST':
        title=request.POST.get('title')
        # date = request.POST.get('date')
        print('title')
        if title:
            obj=models.TODO.objects.get(srno=srno)
            obj.title=title
            # obj.date = date
            obj.save()
            user=request.user
            return redirect('/todopage')
    
    obj=models.TODO.objects.get(srno=srno)
    return render(request,'edit_todo.html',{'obj':obj})

@login_required(login_url='/login')
def delete_todo(request,srno):
    obj=models.TODO.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

def signout(request):
    logout(request)
    return redirect('/user_login')
        