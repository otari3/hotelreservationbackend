from django.db import models,connection,transaction
from shared import models as base_model,erros
from hotels.models import Hotels  

# Create your models here.

class User(models.Model):
  name = models.TextField()
  personal_id = models.IntegerField(db_index=True)
  hotel = models.ForeignKey(Hotels,on_delete=models.CASCADE)
  class Meta:
    unique_together = ('hotel', 'personal_id')
  
  @staticmethod
  def insert_user(user):
    query ="""WITH up as( 
            INSERT INTO users_user (name,personal_id,hotel_id)  
            VALUES ('oto',6,1)
            ON CONFLICT(personal_id,hotel_id) DO NOTHING  
            RETURNING id
            )
            SELECT * FROM up
            UNION(  
            SELECT id FROM users_user
            WHERE personal_id = 6 AND hotel_id =1
          );"""
    pass
    
    
