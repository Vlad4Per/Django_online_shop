from django.shortcuts import render

def login(request):
    context = {

    }
    return render(request, 'users/login.html', context=context)


def signup(request):
    context = {

    }
    return render(request, 'users/signup.html', context=context)


def profile(request):
    context = {

    }
    return render(request, 'users/profile.html', context=context)

def logout(request):
    ...