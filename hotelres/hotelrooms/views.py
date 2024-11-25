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
      hotel_id = getattr(request,'hotel_id',None)
      data = json.loads(request.body)
      HotelRooms.adding_rooms(data,hotel_id['hotel_id'])
      return JsonResponse({'sucsefuly':'Rooms Has Been Added'},status=200)
    except Exception as e:
      return erros.handel_errors(e,'/hotelrooms/views/adding_rooms')
  else:
    return JsonResponse({'error':f'method should be POST'},status=405)
@csrf_exempt
def updating_rooms(request):
  if request.method == "PUT":
    try:
      hotel_id = getattr(request,'hotel_id',None)
      data = json.loads(request.body)
      HotelRooms.update_rooms(data,hotel_id['hotel_id'])
      return JsonResponse({'sucsefuly':'Rooms Has Been Updated'},status =204)
    except Exception as e:
      return erros.handel_errors(e,'hotelrooms/views/updating_rooms')
  else:
    return JsonResponse({'error':f'method should be PUT'},status=405)

def select_all_rooms(request):
  if request.method == "GET":
    try:
      hotel_id = getattr(request,'hotel_id',None)
      return JsonResponse({'rooms':HotelRooms.get_all_rooms(hotel_id['hotel_id'])},status=200)
    except Exception as e:
      return erros.handel_errors(e,'hotelrooms/views/select_all_rooms')
  else:
    return JsonResponse({'error':f'method should be GET'},status=405)
@csrf_exempt
def delete_room(request,id):
  if request.method == 'DELETE':
    try:
      hotel_id = getattr(request,'hotel_id',None)
      HotelRooms.delete_room(id,hotel_id['hotel_id'])
      return JsonResponse({'sucsefuly':'Rooms Has Been Deleted'},status = 204)
    except Exception as e:
      return erros.handel_errors(e,'hotelrooms/views/delete_room')
  else:
    return JsonResponse({'error':f'method should be DELETE'},status=405)
def get_room_info(request):
  if request.method =='GET':
    try:
      hotel_id = getattr(request,'hotel_id',None)
      data = HotelRooms.get_room_info(hotel_id['hotel_id'])
      return JsonResponse({'rooms':data},status=200)
    except Exception as e:
      return erros.handel_errors(e,'hotelroom/views/get_room_info')
    
    
  