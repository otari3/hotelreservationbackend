from django.urls import path
from . import views

urlpatterns = [path('inserthotel/',views.insert_in_hotel,name='insert_in_hotel'),
               path('get-hotel/<int:id>/',views.get_hotel,name='get_hotel'),]