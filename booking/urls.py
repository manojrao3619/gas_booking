from django.conf.urls import url 
from .views import booking, cancelBooking
 
urlpatterns = [ 
    url(r'^booking$', booking),
    url(r'^cancel$', cancelBooking)
    ]