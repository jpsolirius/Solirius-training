from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth

def dashboard(request):
    return render(request, 'users/dashboard.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
            
        else:
            messages.success(request, ('There was an error logging in'))
            return redirect('login')
    else:
        return render(request, 'registration/login_user.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('dashboard')
 

""" def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form}) """

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken.')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                logout(request)
                new_user = authenticate(request, username=username, password=password1)
                login(request, new_user)
                return redirect('dashboard')
                messages.info(request, 'Account created.')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('signup')
    else:
        return render(request, 'registration/signup.html')