from django.shortcuts import render, redirect
from accounts.forms.CustomUserRegisterForm import CustomUserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.forms.CustomLoginForm import CustomLoginForm


def signin(request):
    if request.user.is_authenticated:
        return redirect('shop:home')
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'You are successfully logged in')
                return redirect('dashboard:home')
            else:
                messages.error(request, 'Incorrect username or password.')
        else:
            messages.error(request, 'Please correct the errors in the form.')
               
    else:
        form = CustomLoginForm()
    return render(request, 'accounts/signin.html', {"form": form})

def signup(request):
    if request.user.is_authenticated:
        return redirect('shop:home')
    if request.method == "POST":
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are successfully registered')
            return redirect('accounts:signin')
    else:
        form = CustomUserRegisterForm()
    return render(request, 'accounts/signup.html', {'form':form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("shop:home")