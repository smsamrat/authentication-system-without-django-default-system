
from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='singup'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logout, name='logout')
]