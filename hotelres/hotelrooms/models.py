from django.db import models,connection,transaction
from shared import models as base_model,erros
from hotels import models as hotel_model

# Create your models here.

class HotelRooms(models.Model):
  type = models.TextField(max_length = 30)
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
            SELECT room_number,id,price
            FROM hotelrooms_hotelrooms
            WHERE hotel_id = %s
    """
    try:
      with transaction.atomic():
          return base_model.Data_base_handeler.select_all(query,(hotel_id,))
    except:
      raise
        
    
