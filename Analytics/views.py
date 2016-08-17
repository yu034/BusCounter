# coding: utf8
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.core.context_processors import csrf


# Create your views here.
def main(request):
    args = {}
    args.update(csrf(request))
    # ... view code here
    return render_to_response("analytics.html", args)