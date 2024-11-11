from django.db import models
from shared import models as base_model,erros

# Create your models here.
class Hotels(models.Model):
  name = models.TextField()
  address = models.TextField()
  database_handeler = base_model.Data_base_handeler
  def register_hotel(self):
    query = """INSERT INTO hotels_hotels (name,address)
               VALUES (%s,%s);"""
    try:
      return self.database_handeler.execute_query(query,(self.name,self.address))
    except erros.DataBaseErrors.ExecuteQuery:
      raise
      
  @staticmethod
  def get_hotel(id):
    query = """ SELECT * FROM hotels_hotels 
                WHERE id = %s;"""
    try:
      return base_model.Data_base_handeler.select_one(query,(id,))
    except erros.DataBaseErrors.FormatingError:
      raise
    except erros.DataBaseErrors.SelectOneError:
      raise
    