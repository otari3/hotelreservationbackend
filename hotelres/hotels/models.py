import uuid
from django.db import models,connection,transaction
from shared import models as base_model,erros
import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Hotels(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  email = models.TextField(unique =True)
  password = models.TextField()
  name = models.TextField(unique =True)
  address = models.TextField()
  database_handeler = base_model.Data_base_handeler
  def register_hotel(self):
    query = """INSERT INTO hotels_hotels (id,email,password,name,address)
               VALUES (%s,%s,%s,%s,%s);"""
    try:
      hashed_password = make_password(self.password)
      return self.database_handeler.execute_query(query,(self.id,self.email,hashed_password,self.name,self.address))
    except erros.DataBaseErrors.ExecuteQuery:
      raise
    except Exception as e:
      raise(f'error from --> hotels/models/register_hotel {e}')
      
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
  @staticmethod
  def login(user):
    query = """ SELECT email,password FROM hotels_hotels
                WHERE email = %s
                """
    with transaction.atomic():
      with connection.cursor() as cursor:
        try:
          cursor.execute(query,(user['email'],))
          auth_user = cursor.fetchone()
          if auth_user:
            if check_password(user['password'],auth_user[1]):
              encoded_jwt = jwt.encode({'email':auth_user[0],'password':auth_user[1]},settings.JWT_SECRET_KEY,algorithm="HS256")
              return encoded_jwt
            else:
              raise
          else:
            raise
        except:
          raise Exception('Wrong login Inforamtion')
              
    
    