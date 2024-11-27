from django.db import models,connection,transaction
from shared import models as base_model,erros
from hotels.models import Hotels  


# Create your models here.

class User(models.Model):
  name = models.TextField(null=False)
  personal_id = models.TextField(db_index=True,null=False)
  hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
  class Meta:
    unique_together = ('hotel', 'personal_id')
  
  @staticmethod
  def insert_user(user,hotel_id):
    if not (user['name'] and user['personal_id']):
      raise ValueError('there cant be empty values on users')
    query ="""WITH up as( 
            INSERT INTO users_user (name,personal_id,hotel_id)  
            VALUES (%s,%s,%s)
            ON CONFLICT(personal_id,hotel_id) DO NOTHING  
            RETURNING id
            )
            SELECT * FROM up
            UNION(  
            SELECT id FROM users_user
            WHERE personal_id = %s AND hotel_id =%s
          );"""
    try:
      user_id = base_model.Data_base_handeler.select_one(query,(user['name'],user['personal_id'], 
                                                          hotel_id,user['personal_id'],hotel_id))
      return user_id
    except Exception:
      raise
    
    
