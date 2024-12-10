from django.urls import path
from . import views
urlpatterns = [path('get_avalible_rooms/',views.get_avalible_rooms,name='get_avalible_rooms'),
               path('filter_rooms/',views.get_filtered_rooms,name='fiter_rooms'),
               path('get_rooms/',views.get_specific_rooms,name='get_specific_rooms'),
               path('move_to_hotel/<int:id>/', views.move_to_hotel, name='product_detail'),
               path('move_to_report/<int:id>/', views.move_to_report, name='move_to_report'),
               path('delete_from_reservation/<int:id>', views.delete_from_reservation, name='delete_from_reservation'),
               ]