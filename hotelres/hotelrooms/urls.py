from django.urls import path
from . import views

urlpatterns = [path('insertrooms/',views.adding_rooms,name='adding_rooms'),
               path('updaterooms/',views.updating_rooms,name='updating_rooms'),
               path('selectallrooms/',views.select_all_rooms,name='select_all_rooms'),
               path('deleteroom/<int:id>',views.delete_room,name='delete_room'),
               path('get-room-info/',views.get_room_info)]