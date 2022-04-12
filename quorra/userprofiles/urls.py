from django.urls import path
from . import views

app_name = "userprofiles"

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.userRegistration,name="register"),
    path('login/',views.userLogin, name="login"),
]
