from django.http import JsonResponse
from shared import erros
from django.views.decorators.csrf import csrf_exempt
from .models  import Reservation
@csrf_exempt
def get_avalible_rooms(request):
  if request.method == 'GET':
    try:
      hotel_id = getattr(request,'hotel_id',None)
      return JsonResponse({'rooms':Reservation.get_avalible_rooms(hotel_id['hotel_id'])},status=200)
    except Exception as e:
      return erros.handel_errors(e,'/resrevation/views/get_avalible_rooms')