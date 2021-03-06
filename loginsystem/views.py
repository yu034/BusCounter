# coding: utf8
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.core.context_processors import csrf


# Create your views here.

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'Неверный логин или пароль'
    return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')




