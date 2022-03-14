from django import forms
from django.urls import reverse
from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Contactus
from .forms import ContactusForm
from django.contrib import messages


# Create your views here.

def contact(request):

  if request.method == "POST":
    form = ContactusForm(request.POST)
    if form.is_valid():
      new_name = form.cleaned_data['name']
      new_email = form.cleaned_data['email']
      new_message = form.cleaned_data['message']

      new_contacat = Contactus(name = new_name, email = new_email, message = new_message)
      new_contacat.save()

      messages.success(request, 'با موفقیت ثبت شد')
      return HttpResponseRedirect(reverse('contact:contact_url'))
      
  else:
    form = ContactusForm()
      

  return render(request, 'contact/contact.html')
    