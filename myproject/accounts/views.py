from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':

        if request.POST['password'] == request.POST['password2']:
            
            try:
                user = User.objects.get(username=request.POST['user'])
                return render (request, 'accounts/signup.html', {'error': 'Username has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user( request.POST['user'], request.POST['password'] )
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error' : 'username or password is incorrect.'})
    
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    else:
        return render(request, 'accounts/signup.html')