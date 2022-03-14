from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def unauthenticated_user(view_func):
    def wrapper_func(request , *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'شما وارد حساب کاربری خود شده اید')
            return redirect('users:reservations')
        else : 
         return view_func(request,*args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            return view_func(request,*args, **kwargs)
        return wrapper_func
    return decorator
