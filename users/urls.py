from reservation.models import reservation
from django.urls import path
from . import views
from reservation.views import reservations

app_name = 'users'

urlpatterns = [
    
    path('',views.signup_view,name = 'signup'),
    path('login',views.login_view,name = 'login'),
    path('logout',views.LogoutUser,name = 'logout'),
    path(r'reservation/',reservations,name='reservations'),
    path('user/',views.user_views,name='userviews')
]
