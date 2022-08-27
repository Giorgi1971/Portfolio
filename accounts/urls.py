from django.urls import path
from .views import *


app_name = 'accounts'

urlpatterns = [
    path('', index, name='home'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('logout_f/', logout_f, name='logout'),
    path('login_f/', my_login, name='login'),
    path('register_f/', register, name='register'),
    path('register/', SignUpView.as_view(), name='register_view'),
]
