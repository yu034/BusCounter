from django.shortcuts import render,render_to_response
from django.contrib import auth

# Create your views here.

def main(request):
    return render_to_response('main.html', {'username': auth.get_user(request).username})

def products(request):
    return render_to_response('products.html', {'username': auth.get_user(request).username})

def about_us(request):
    return render_to_response('about.html', {'username': auth.get_user(request).username})