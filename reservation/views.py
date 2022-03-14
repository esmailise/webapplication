from django.shortcuts import render , HttpResponseRedirect
from .forms import ReservationForm
from works.models import Category
from django.contrib import messages
from django.urls import reverse
from django.utils import timezone
from .models import reservation
# Create your views here.


def reservations(request):
    reservation_date = timezone.now()
    categorys_list = Category.objects.all()
    
    if request.method == "POST":

        current_user = request.user
        all_reservation = reservation.objects.filter(user = current_user,status =False)

        reserve_form = ReservationForm(request.POST)       

        if reserve_form.is_valid():
            
            date = reserve_form.cleaned_data['data']
            time = reserve_form.cleaned_data['time']
            count_date = reservation.objects.filter(data = date).count()
            count_time = reservation.objects.filter(time = time).count()
            
            if count_date > 0 and  count_time > 0 :
                messages.success(request, 'زمانی جلوتر از زمان سیستم انتخاب کنید')
                return HttpResponseRedirect(reverse('reservation:reservationview'))

            elif count_date > 2:
                messages.success(request, 'تاریخی جلوتر از تاریخ سیستم انتخاب کنید')
                return HttpResponseRedirect(reverse('reservation:reservationview'))

            elif all_reservation:
                messages.success(request, 'شما یک کار انجام نشده دارید')
                return HttpResponseRedirect(reverse('reservation:reservationview')) 

            else:
                pk = reserve_form.save()

                pk.user = request.user
                pk.save()

                messages.success(request, ' {} : رزرو با موفقیت ثبت شد شماره پیگیری شما  '.format(pk.id))
                return HttpResponseRedirect(reverse('reservation:reservationview'))
        else :
            messages.success(request, 'ورودی های خود را با دقت وارد فرمایید') 
            return HttpResponseRedirect(reverse('reservation:reservationview')) 
                
    else:
        reserve_form = ReservationForm()
        
    contex={
        "list":categorys_list,
        "reservation_date":reservation_date,
    }

    return render(request,'reservation/reservation.html',contex)

