from django.shortcuts import render, redirect
from django.contrib import messages

def user_authenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('index')
    return wrapper

def user_unauthenticated(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper