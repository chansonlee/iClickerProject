from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def index(request):
    return render(request, 'student/index.html', {})
    
def user_list(request):
    return render(request, 'student/user_list.html')


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('student:user_list'))
        else:
            print(form.errors)
    return render(request, 'student/log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('student:log_in'))

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('student:log_in'))
        else:
            print(form.errors)
    return render(request, 'student/sign_up.html', {'form': form})