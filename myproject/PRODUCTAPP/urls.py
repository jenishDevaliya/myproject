from django.conf import path

from ProductAPP.views import Homeview, Productview

urlpatterns = [
    path('home/',Homeview),
    path('product/',Productview),
]