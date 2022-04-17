from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *


def profile(request):
    return render(request, 'account/profile.html')


# @TODO: Create register View

def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username},Account created; Please logIn!')
            return redirect('login')
    else :
        form = RegForm()
    return render(request, 'account/register.html', {'form': form})

def login(request):
    pass


def logout(request):
    pass