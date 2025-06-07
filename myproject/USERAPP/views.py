from django.shortcuts import render

# Create your views here.
def Loginview(request):
    return render(request,'login.html');

def Signupview(request):
    return render(request,'signup.html');