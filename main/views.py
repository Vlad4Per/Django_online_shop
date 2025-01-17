from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title':'Home Page',
        'content':'Home Page',
        'list':[0,1,2]
    }
    return render(request, 'main/index.html', context)

def info(request):
    return HttpResponse("Info Page")