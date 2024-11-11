from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import HotelRooms
from shared import erros

# Create your views here.
@csrf_exempt
def adding_rooms(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      HotelRooms.adding_rooms(data)
      return JsonResponse({'sucsefuly':'Rooms Has Been Added'},status=200)
    except Exception as e:
      return erros.handel_errors(e,'/hotelrooms/views/adding_rooms')
  else:
    return JsonResponse({'error':f'method should be POST'},status=405)
@csrf_exempt
def updating_rooms(request):
  if request.method == "PUT":
    try:
      data = json.loads(request.body)
      HotelRooms.update_rooms(data)
      return JsonResponse({'sucsefuly':'Rooms Has Been Updated'},status =204)
    except Exception as e:
      return erros.handel_errors(e,'hotelrooms/views/updating_rooms')
  else:
    return JsonResponse({'error':f'method should be PUT'},status=405)

def select_all_rooms(request,id):
  if request.method == "GET":
    try:
      return JsonResponse({'rooms':HotelRooms.get_all_rooms(int(id))},status=200)
    except Exception as e:
      return erros.handel_errors(e,'hotelrooms/views/select_all_rooms')
  else:
    return JsonResponse({'error':f'method should be GET'},status=405)
@csrf_exempt
def delete_room(request,id,hotelid):
  if request.method == 'DELETE':
    try:
      HotelRooms.delete_room(id,hotelid)
      return JsonResponse({'sucsefuly':'Rooms Has Been Deleted'},status = 204)
    except Exception as e:
      return erros.handel_errors(e,'hotelrooms/views/delete_room')
  else:
    return JsonResponse({'error':f'method should be DELETE'},status=405)
    
    
  