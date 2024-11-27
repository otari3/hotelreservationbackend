from django.db import models,connection,transaction
from shared import models as base_model,erros
from hotels import models as hotel_model

# Create your models here.

class HotelRooms(models.Model):
  type = models.TextField()
  price = models.IntegerField()
  room_number = models.IntegerField()
  imgs = models.TextField() 
  hotel = models.ForeignKey(hotel_model.Hotels,on_delete=models.CASCADE)
  class Meta:
    unique_together = ['hotel', 'room_number']
  @staticmethod
  def adding_rooms(room,hotel_id):
    query = """INSERT INTO hotelrooms_hotelrooms (type,price,room_number,hotel_id,imgs)
               VALUES (%s,%s,%s,%s,%s);"""
    try:
      with transaction.atomic():
        with connection.cursor() as cursor:
            params = (room['type'],room['price'],room['room_number'],hotel_id,room['imgs'])
            cursor.execute(query,params)
    except Exception as e:
      raise erros.DataBaseErrors.AddinRoomsError(f'There Seems to Be Some Kind of Error --> From adding_rooms {e}')
  @staticmethod
  def update_rooms(room,hotel_id):
      query = """ 
      UPDATE hotelrooms_hotelrooms
      SET type = %s,price = %s,room_number = %s,imgs = %s
      WHERE id = %s AND hotel_id = %s;"""
      try:
        with transaction.atomic():
          with connection.cursor() as cursor:
              params = (room['type'],room['price'],room['room_number'],room['imgs'],room['id'],hotel_id)
              cursor.execute(query,params)
      except Exception as e:
        raise erros.DataBaseErrors.UpdatingRoomsError(f'There Seems to Be Some Kind of Error -->  /hotelrooms/models/updating_rooms {e}')
  @staticmethod
  def get_all_rooms(id):
    query = """SELECT r.id,r.type,r.price,r.room_number,r.imgs
               FROM hotelrooms_hotelrooms as r
               WHERE r.hotel_id = %s
               ORDER BY r.price ASC;"""
    try:
      return base_model.Data_base_handeler.select_all(query,(id,))
    except erros.DataBaseErrors.FormatingError:
      raise
    except erros.DataBaseErrors.SelectAll:
      raise
  @staticmethod
  def delete_room(id,hotelid):
    query = """DELETE FROM hotelrooms_hotelrooms   
              WHERE id = %s AND hotel_id = %s"""
    try:
      base_model.Data_base_handeler.execute_query(query,(int(id),hotelid))
    except erros.DataBaseErrors.ExecuteQuery:
      raise
  @staticmethod
  def get_room_info(hotel_id):
    query = """
 WITH  table_expersion AS( 
        SELECT r.room_id,generate_series( 
          r.check_in::date,
          r.check_out::date,
          '1 day'::interval
        ) AS booked_dates
        from reservation_reservation r
        WHERE r.hotel_id = %s
        )
        SELECT room.room_number,room.price,room.id, 
        array_agg(te.booked_dates::date) AS booked_dates
        FROM hotelrooms_hotelrooms room
        LEFT JOIN table_expersion te 
        ON te.room_id=room.id
        WHERE room.hotel_id = %s
        GROUP BY room.room_number,room.price,room.id;
    """
    try:
      with transaction.atomic():
          return base_model.Data_base_handeler.select_all(query,(hotel_id,hotel_id))
    except:
      raise
        
    
