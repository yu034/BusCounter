from django.shortcuts import render,render_to_response
from django.contrib import auth
from .models import page

# Create your views here.

def main(request, page_alias):

    return render_to_response('main.html', {'username': auth.get_user(request).username})



