from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render (request, 'accounts/signup.html', {'error':'Username is already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render (request, 'accounts/welcome.html')
        else:
            return render (request, 'accounts/signup.html', {'error':'Passwords did not match'})
    else:
        return render (request, 'accounts/signup.html')

def loginview(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST["next"])
            return render(request, 'accounts/profile.html')
            # return redirect('home')   #login page
            # return redirect('profile')   #login page
            #return render (request, 'accounts/login.html', {'error':'Logged in succesfully'})
        else:
            return render (request, 'accounts/login.html', {'error':'Username and password did not match'})
    else:
        return render (request, 'accounts/login.html')

def logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def profile(request):
    return render(request, 'accounts/profile.html')

def welcome(request):
    return render(request, 'accounts/welcome.html')