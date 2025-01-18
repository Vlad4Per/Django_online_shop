from django.shortcuts import render

# Create your views here.
def category(request):
    return render(request,'catalog/category.html')

def product(request):
    return render(request,'catalog/product.html')