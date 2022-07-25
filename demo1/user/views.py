
from pdb import post_mortem
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from .models import UserInformation
from user.form import SignUpForm


# Create your views here.

def signupUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #create user and save information
            form.save()
            #auth_login(request,user)
            user = form.cleaned_data.get('username')
            messages.success(request,"Register successful, username: " + user)
            return redirect('/login/')
        else:
         messages.error(request,"unsuccessful")
    else:
        form = SignUpForm()
    context = {'form':form } 
    return render(request,'signup.html',context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect('/home/') 
        else:
            
            messages.info(request,'Your Username and Password is not correct')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/home/')
