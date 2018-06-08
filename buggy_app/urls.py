from django.conf.urls import url
from . import views

app_name = 'buggy_app'

urlpatterns = [

    url(r'^carlist$',views.CarListView.as_view(),name='car_list'),
    url(r'^(?P<pk>\d+)/$',views.CarDetailView.as_view(),name='details'),
    #url(r'^(?P<pk>\d+)/book$',views.booking_create,name='booking_create'),
    url('booking/',views.BookingView.as_view(),name='car_booking'),




]
