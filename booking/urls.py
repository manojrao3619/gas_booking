from django.conf.urls import url 
from .views import booking, cancelBooking, bookingHistory
 
urlpatterns = [ 
    url(r'^booking$', booking),
    url(r'^cancel$', cancelBooking),
    url(r'^history$', bookingHistory),
    ]
