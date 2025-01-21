from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title':'login',
        'form':form,
    }
    return render(request, 'users/login.html', context=context)


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title':'signup',
        'form':form,
    }
    return render(request, 'users/signup.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST,instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'profile',
        'form': form,
    }
    return render(request, 'users/profile.html', context=context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('user:login'))


def users_cart(request):
    return render(request, 'users/users_cart.html')