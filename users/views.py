from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistrationForm


def login(request):
    return render(request,'users/login.html')


def logout(request):
    return render(request,'users/logout.html')


def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get('username')
            messages.success(request,f'Profile created for child { name }!')
            return redirect('home')
    else:
        form=UserRegistrationForm()

    return render(request,'users/register.html',{'form':form})