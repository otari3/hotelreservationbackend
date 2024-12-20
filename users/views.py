from django.http import JsonResponse
from shared import erros
import json
from django.views.decorators.csrf import csrf_exempt
from .models import User
from reservation.models import Reservation


# Create your views here.

@csrf_exempt
def insert_user(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      hotel_id = getattr(request,'hotel_id',None)
      user_id = User.insert_user(data,hotel_id['hotel_id'])
      resvation = Reservation(check_in=data['check_in'],check_out=data['check_out'],user_id=user_id[0]['id'],  
                                price=data['price'],in_hotel=False,nights=data['nights'], 
                                hotel_id=hotel_id['hotel_id'],room_id=data['room_id'])
      resvation.clean()
      resvation.save()
      return JsonResponse({'user':user_id})
    except Exception as e:
      return erros.handel_errors(e,'/users/views/insert_user')
  else:
    return JsonResponse({'error':f'method should be POST'},status=405)
  