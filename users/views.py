from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from reservation.models import reservation
from works.models import works,Category
# Create your views here.

def signup_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'شما وارد حساب کاربری خود شده اید')
        return redirect('users:reservations')       
    else : 
        if request.method == 'POST':
            form_username = request.POST['username']
            form_email = request.POST['email']
            form_password1 = request.POST['password1']
            form_password2 = request.POST['password2']
            if form_password1 == form_password2 : 
                if User.objects.filter(username= form_username).exists():
                    messages.info(request,'این نام کاربری قبلا ثبت شده است')
                    return redirect('users:signup')

                elif User.objects.filter(email=form_email).exists():
                    messages.info(request,'این ایمیل قبلا ثبت شده است')
                    return redirect('users:signup')

                else:
                    user  =  User.objects.create_user(username = form_username , email = form_email, password = form_password1)
                    user.save()
                    
                    messages.success(request,'حساب شما با موفقیت ثبت شد')
                    return redirect('users:login')
            else:
                messages.info(request,'گذرواژه ها یکی نیستند')  
                return redirect('users:signup')
        
        else:
            return render(request, 'users/signup.html')

def login_view(request):
    if request.user.is_authenticated:
        messages.success(request, 'شما وارد حساب کاربری خود شده اید')
        return redirect('users:reservations')
    else : 
        if request.method == 'POST':
            form_usrename = request.POST.get('username')
            form_password = request.POST.get('password')
            user = authenticate(request,username = form_usrename,password = form_password )
            if user is not None:
                login(request,user)
                messages.success(request,'با موفقیت وارد شدید')
                return redirect('users:reservations')            
            else:
                messages.info(request,'رمز یا نام کاربری اشتباه است')
                return redirect('users:login')
        else : 
            return render(request,'users/login.html')

def LogoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('users:login')
        
def user_views(request):
    if request.user.is_authenticated :
        current_user = request.user
        works_detail = reservation.objects.all().filter(user = current_user)
        works_list = works.objects.all()
        category = Category.objects.all()
    else :
        messages.info(request,'ابتدا وارد حساب کاربری خود شوید')
        return redirect('users:login')

    contex ={
        'user':current_user,
        'works_detail':works_detail,
        'works' : works_list, 
        'category' : category,
    }
    return render(request,'users/user.html',contex)
