from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from authentication.models import Userinfo




# Create your views here.
#create all views of templets for your wiew


def home(request):
    return render(request,"authentication/index.html")



def signup(request):
    if request.method == "POST":
        username= request.POST.get('Uname')
        #username=request.POST['Uname']
        #email=request.POST['emai']
        email= request.POST.get('email')
        #password=request.POST['pswd']
        password= request.POST.get('pswd')
        


        myuser=User.objects.filter( username = username )
        if myuser.exists():
            return HttpResponse('Username alrady taken, Please try a unique Username')
        
        myuser =User.objects.create_user(username,email,password)
        myuser.first_name = username
        myuser.save()
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            u_name = user.username
            

        
        
        

        #messages.success(request,"Your account craeted.")
        return render(request,"authentication/regst.html",{'u_name':u_name})







    return render(request,"authentication/signup.html")


def signin(request):
    if request.method== 'POST':
        username= request.POST.get('Uname')
        password= request.POST.get('pswd')
        user= authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"userdash/u_dash.html", {'fname':fname})

        else:
            
            return HttpResponse('Incorrect username or password!!, go back and login again')
            





    return render(request,"authentication/signin.html")

@login_required(login_url="/signin")
def userdetails(request):
    if request.method=="POST":
    
         
         name=request.POST.get('fullname')
         ftrname=request.POST.get('fathername')
         mtrname=request.POST.get('mothersname')
         username1=request.POST.get('username_auser')
         password=request.POST.get('fullname')
         email=request.POST.get('email')
         gender=request.POST.get('gender')
         picfil=request.POST.get('picfil')
         dob=request.POST.get('DOB')
         qullification= request.POST.get('qullification')
         department= request.POST.get('department')
         phonenumber1= request.POST.get('phonenumber1')
         phonenumber2= request.POST.get('phonenumber2')
         phonenumber3= request.POST.get('phonenumber3')
         pstate= request.POST.get('pstate')
         pcity= request.POST.get('pcity')
         pzip= request.POST.get('pzip')

         user=Userinfo(userinfo_name=name,userinfo_Uname=username1,userinfo_Ftname=ftrname,userinfo_Mtname=mtrname,userinfo_email=email,userinfo_userpic=picfil,userinfo_phoneno1=phonenumber1,userinfo_phoneno2=phonenumber2,userinfo_phoneno3=phonenumber3,userinfo_password=password,userinfo_gender=gender,userinfo_Edulvl=qullification,userinfo_Expedu=department,userinfo_State=pstate,userinfo_City=pcity,userinfo_Zip=pzip,userinfo_DoB=dob,)
         user.save()
         #return HttpResponse('Welcome TO Our Family')
         return render(request,"authentication/signin.html")


def signout(request):
    logout(request)
    return HttpResponse('Its a batter Conve with us! THANKS')

    


def preatics(request):
    return render(request,"authentication/preatics.html")


def about(request):
    return render(request,"authentication/about.html")


def contact(request):
    return render(request,"authentication/contact.html")



def design(request):
    return render(request,"authentication/design.html")

def regst(request):
    return render(request,"authentication/regst.html")

@login_required(login_url="/signin")
def u_dash(request):
    return render(request,"userdash/u_dash.html")
