from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def signup(request):
    return render(request, 'signup.html')
def signin(request):
    return render(request, 'signin.html')
def contactus(request):
    return render(request, 'contactus.html')
def signuppage(request):

    if request.method=="POST":
        fname = request.POST['firstname']
        
        lname = request.POST['lastname']
        unm = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        try:
            user = User.objects.get(username = unm)
            return render(request,'signup.html')
        except:
            user = User.objects.create_user(first_name = fname,last_name = lname, username = unm, email = email, password = pwd)
            user.save()
            return render(request,'signin.html')
    else:
        return render(request, 'signup.html')
def signinpage(request):
    if request.method =="POST":
        unm =request.POST['username']
        pwd =request.POST['password']

        user = auth.authenticate(username = unm, password = pwd) 
        if user is not None:
            auth.login(request,user)
            return redirect('userhome')
        else:
            return render(request,'Signup.html')
    else:
        return render(request, signin.html)
def userhome(request):
    return render(request, 'userhome.html')
def logout(request):
    auth.logout(request)
    return render(request, 'home.html')
def contactuspage(request):
    if request.method=="POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        comment = request.POST['comment']

        contact = Contact(fname=fname,lname=lname, email=email,mobile=mobile,comment=comment)
        contact.save()
        return render(request,'home.html')
    else:
        return render(request, 'contactus.html')
