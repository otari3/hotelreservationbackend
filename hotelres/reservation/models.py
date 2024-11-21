from django.db import models,connection,transaction
from users.models import User
from hotels.models import Hotels
from hotelrooms.models import HotelRooms
from shared import models as handeler
import json
from psycopg2 import sql


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
    unique_together = ('check_in','check_out','hotel','room')
    indexes = [
        models.Index(fields=['check_in', 'check_out','user','hotel','room'])
    ]

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
  @staticmethod
  def searchin_reservation_info(where_query,haveing_query,hotel_id,params):
    where_clause = sql.SQL("AND {}").format(sql.SQL(where_query)) if where_query else sql.SQL("")
    haveing_clause = sql.SQL("AND {}").format(sql.SQL(haveing_query)) if haveing_query else sql.SQL("")
    query = """
              WITH order_reservation as (SELECT  
                      array_agg(r.id) AS reservation_ids,array_agg(rooms.room_number) AS rooms,  
                      sum(r.nights*r.price) AS total, r.check_in,r.check_out,u.personal_id,u.name,
                      ROW_NUMBER() OVER(ORDER BY r.check_in) as pagination_ids
                      FROM reservation_reservation r  
                      INNER JOIN hotelrooms_hotelrooms rooms ON r.room_id = rooms.id  
                      INNER JOIN users_user u ON r.user_id = u.id
                      WHERE r.hotel_id= %s {where_clause}
                      GROUP BY r.check_in,r.check_out,u.id
                      HAVING TRUE {haveing_clause})
              SELECT * FROM order_reservation 
              LIMIT 100;
              """.format(where_clause=where_clause.as_string(connection),  
                        haveing_clause=haveing_clause.as_string(connection))
    try:
     with connection.cursor() as cursor:
       cursor.execute(query,[hotel_id,*params])
       data = cursor.fetchall()
       desc = cursor.description
       return handeler.Data_base_handeler.format_information(data,desc)
    except  Exception as e:
      raise
  @staticmethod   
  def get_avalible_rooms(hotel_id):
    query = """WITH reserved_dates_rooms AS (SELECT room_id, jsonb_build_object( 
               'check_in',check_in,
               'check_out',check_out,
               'user_name',u.name,
               'user_id',u.personal_id
               ) AS reservation_info
               FROM reservation_reservation r
               INNER JOIN users_user u ON  
               r.user_id = u.id 
               WHERE r.hotel_id = %s)
               SELECT r.room_number, array_agg(rdr.reservation_info) AS dates
               FROM reserved_dates_rooms rdr
               RIGHT JOIN hotelrooms_hotelrooms r
               ON rdr.room_id = r.id
               WHERE r.hotel_id = %s
               GROUP BY r.room_number;
              """
    try:
      data = handeler.Data_base_handeler.select_all(query,(hotel_id,hotel_id))
      serilazed_data = [{"room_number":r['room_number'],  
                                   "dates":[json.loads(date) if date else None 
                                                            for date in r['dates']]}
                                                            for r in data]
      return serilazed_data
    except:
      raise
  @staticmethod
  def get_all_booked_dates(hotel_id):
    query = """
        WITH  table_expersion AS( 
        SELECT room.room_number,generate_series( 
          r.check_in::date,
          r.check_out::date,
          '1 day'::interval
        )::date AS booked_dates
        from reservation_reservation r 
        INNER JOIN hotelrooms_hotelrooms room ON room.id = r.room_id 
        WHERE r.hotel_id = %s
        )
        SELECT te.room_number,array_agg(te.booked_dates)
        FROM table_expersion as te
        GROUP BY te.room_number;
    """
    
        