from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def mainpage(request):
    products= Product.objects.all()
    return render(request, 'products/index.html',
                  {'products': products})


def new(request):
    return HttpResponse("New Products")