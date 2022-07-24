from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
# Create your views here.
from user.form import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

