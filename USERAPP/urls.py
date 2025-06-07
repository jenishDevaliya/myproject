from django.urls import path

from USERApp.views import Loginview,Signupview

urlpattern=[
    path('login/',Loginview),
    path('Signup/',Signupview),
]