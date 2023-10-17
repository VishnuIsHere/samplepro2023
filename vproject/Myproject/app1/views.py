from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import*
from . form import gameform
from app1.models import Private

# Create your views here.
def signup1(request):
  
        if request.method== 'POST':
           username=request.POST.get('username')
           email=request.POST.get('email')
           password=request.POST.get('password')
           c_password=request.POST.get('cpswd')
           if password==c_password:
               if User.objects.filter(username=username,email=email).exists():
                   messages.info(request,'username already taken')
                   print('already have')
               else:
                   new_user=User.objects.create_user(username,email,password)
                   new_user.save()
                   return redirect(login1)
           else:
               print('wrong password')
        return render (request,'signup.html')
        

def login1(request):

        if request.method== 'POST':
           username=request.POST.get('username')
           password=request.POST.get('password')
           user = authenticate(request,username=username,password=password)

     
           if user is not None:
               login(request,user)
               return redirect(fileupload)
      
           else:
               messages.info(request,'user not exist')
               print('user not exist')
               return redirect(login1)
        return render (request,'login.html')







def adminlogin(request):

        if request.method== 'POST':
           username=request.POST.get('username')
           password=request.POST.get('pass')
           obj=Private.objects.all()
           if Private.objects.filter(user=username,password=password).exists():
                   messages.info(request,'username already taken')
                   print('already have')
                   return redirect(upload)

        #    user = authenticate(request,username=username,password=password)

     
        #    if user is not None:
        #        login(request,user)
        #        return redirect(upload)
      
           else:
               messages.info(request,'user not exist')
               print('user not exist')
               return redirect(adminlogin)
        return render (request,'adminlogin.html')





@login_required
def home1(request):
    return render(request,'home.html')


@login_required
def userlogout(request):
     
    logout(request)
    return redirect(login1)
 

def upload(request):
     form= gameform()
     if (request.method=='POST'):
          form=gameform(request.POST,request.FILES)
          if form.is_valid():
               form.save()
               return redirect(fileupload)
     return render(request,'home.html',{'forms':form})


def fileupload(request):
     g={
          
       'dw1': Games.objects.all()

     }
     return render (request,'fileupload.html',g)

     