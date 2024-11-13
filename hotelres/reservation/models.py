from django.db import models
from users.models import User
from hotels.models import Hotels
from hotelrooms.models import HotelRooms

# Create your models here.

class Reservation(models.Model):
  check_in = models.DateField()
  check_out = models.DateField()
  user_id = models.ForeignKey(User,on_delete=models.CASCADE)
  price = models.IntegerField()
  in_hotel = models.BooleanField()
  nights = models.IntegerField()
  hotel_id = models.ForeignKey(Hotels,on_delete=models.CASCADE)
  room_id = models.ForeignKey(HotelRooms,on_delete=models.CASCADE)
  class Meta:
    unique_together = ('check_in','check_out','hotel_id','room_id')