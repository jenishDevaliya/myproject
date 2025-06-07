from django.shortcuts import render

# Create your views here.
def Homeview(request):
    return render(request,'home.html');

def Productview(request):
    return render(request,'product.html');
