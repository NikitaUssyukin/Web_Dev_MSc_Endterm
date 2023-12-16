from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# def index(request): 
#     return HttpResponse("You're at Posts index.")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login/')  # redirect to login page
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('')  # redirect to home
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})
