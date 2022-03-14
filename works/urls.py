from django.urls import path, re_path
from . import views
from reservation.views import reservations
from blog.views import blog_list
from contact.views import contact

app_name = 'works'

urlpatterns = [

    path(r'',views.works_list,name='works_list'),
    path(r'reservation/',reservations,name='reservations'),
    path(r'blog/',blog_list,name='blog'),
    path(r'contact/',contact,name='contact_url')
] 