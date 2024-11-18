from django.urls import path
from . import views
urlpatterns = [path('get_avalible_rooms/',views.get_avalible_rooms,name='get_avalible_rooms'),
               path('filter_rooms/',views.get_filtered_rooms,name='fiter_rooms')
               ]