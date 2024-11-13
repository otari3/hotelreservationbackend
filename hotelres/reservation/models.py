from django.db import models
from users.models import User
from hotels.models import Hotels
from hotelrooms.models import HotelRooms
from shared import models as handeler

# Create your models here.

class Reservation(models.Model):
  check_in = models.DateField()
  check_out = models.DateField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  price = models.IntegerField()
  in_hotel = models.BooleanField()
  nights = models.IntegerField()
  hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
  room = models.ForeignKey(HotelRooms,on_delete=models.CASCADE)
  class Meta:
    unique_together = ('check_in','check_out','hotel_id','room_id')
  def insert_reservation(self):
    query = """INSERT INTO reservation_reservation  
               (check_in,check_out,user_id,price,in_hotel,nights,hotel_id,room_id)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
            """
    try:
      handeler.Data_base_handeler.execute_query(query,  
                                              (self.check_in,self.check_out,self.user_id, 
                                               self.price,self.in_hotel,self.nights,  
                                               self.hotel_id,self.room_id))
    except:
      raise
        