from urllib.parse import urlparse
import django
from django import views


from django.urls import path,include

from . import views
from account.views import UserRegistrationView,UserLoginView



urlpatterns = [
    path('',views.bhim),
    path('register',UserRegistrationView.as_view(), name='register'),
    path('login',UserLoginView.as_view(), name='login'),
]
