from django.db import connection
from shared import erros

class Data_base_handeler:
  @staticmethod
  def format_information(rows,collums):
    try:
      collums = [col[0] for col in collums]
      formatInformation = [dict(zip(collums,row)) for row in rows]
    except TypeError as typeError:
      raise erros.DataBaseErrors.FormatingError(f'Error from --> format_information u need to pass correct id  {typeError}')
    except Exception as e:
      raise erros.DataBaseErrors.FormatingError(f'Error From --> format_information in data_base_handeler {e}')
    return formatInformation
    
  @staticmethod
  def select_all(query,params):
    with connection.cursor() as cursor:
      try:
        cursor.execute(query,params)
        collums = cursor.description
        rows = cursor.fetchall()
        return Data_base_handeler.format_information(rows,collums)
      except erros.DataBaseErrors.FormatingError:
        raise 
      except Exception as e:
        raise erros.DataBaseErrors.SelectAll(f'Error From --> select_all in data_base_handeler {e}')
  @staticmethod
  def select_one(query,params):
    with connection.cursor() as cursor:
      try:
        cursor.execute(query,params)
        collums = cursor.description
        rows = cursor.fetchone()
        return Data_base_handeler.format_information((rows,),collums)
      except erros.DataBaseErrors.FormatingError:
        raise 
      except Exception as e:
        raise erros.DataBaseErrors.SelectOneError(f'Error From --> select_one in data_base_handeler {e}')
        
  @staticmethod
  def execute_query(query,params):
    with connection.cursor() as cursor:
      try:
        cursor.execute(query,params)
        return {'successful':True}
      except Exception as e:
        raise erros.DataBaseErrors.ExecuteQuery(f'Error From --> execute_query in data_base_handeler {e}')
        
      
    