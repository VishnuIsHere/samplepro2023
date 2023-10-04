from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup1(request):
    if request.user.is_authenticated:
       return render(request,'home.html')
    else:
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
    if request.user.is_authenticated:  
       return render(request,'home.html')
    else:
        if request.method== 'POST':
           username=request.POST.get('username')
           password=request.POST.get('password')
           user = authenticate(request,username=username,password=password)

     
           if user is not None:
               login1(request,user)
               return redirect('home.html')
      
           else:
               messages.info(request,'user not exist')
               print('user not exist')
               return redirect(login1)
        return render (request,'login.html')



def home1(request):
    return render(request,'home.html')
 
