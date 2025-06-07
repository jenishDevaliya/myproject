from django.urls import path

from UserApp.views import Loginview,Signupview

urlpattern=[
    path('login/',Loginview),
    path('Signup/',Signupview),
]