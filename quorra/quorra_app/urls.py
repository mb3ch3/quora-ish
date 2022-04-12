from . import  views
from django.urls import path
from django.shortcuts import render
app_name="quorra_app"

urlpatterns = [
    path('',views.home,name="home")

]
