from django.http import JsonResponse
from shared import erros
from django.views.decorators.csrf import csrf_exempt
from .models  import Reservation
import json
@csrf_exempt
def get_avalible_rooms(request):
  if request.method == 'GET':
    try:
      hotel_id = getattr(request,'hotel_id',None)
      return JsonResponse({'rooms':Reservation.get_avalible_rooms(hotel_id['hotel_id'])},status=200)
    except Exception as e:
       erros.handel_errors(e,'/resrevation/views/get_avalible_rooms')


def get_filtered_rooms(request):
  if request.method == 'GET':
    try:
      hotel_id = getattr(request,'hotel_id',None)
      to_price = request.GET.get('to')
      from_price = request.GET.get('from')
      check_in = request.GET.get('check_in')
      check_out = request.GET.get('check_out')
      search = request.GET.get('search')
      reservation_id = request.GET.get('id')
      in_hotel = request.GET.get('in_hotel')
      dynamic_query_having = []
      dynamic_query_where = []
      params = []
      #TODO MAKE USER ID SEND AS REQUEST BODY
      #SO FROM FRONT END WHEN SOMEONE REFERSE PAGE IT WILL REMOVE PAGINATION
      #WHERE
      if check_in:
        dynamic_query_where.append("r.check_in >= %s" )
        params.append(check_in)
      if check_out:
        dynamic_query_where.append("r.check_out <= %s")
        params.append(check_out)
      if reservation_id:
        dynamic_query_where.append("r.id > %s")
        params.append(reservation_id)
      if search:
        dynamic_query_where.append("(u.name LIKE %s OR u.personal_id LIKE %s)")
        params.append(f"%{search}%")
        params.append(f"%{search}%")
      if in_hotel:
        dynamic_query_where.append("r.in_hotel")
      else:
        dynamic_query_where.append("NOT r.in_hotel")
    ##HAVING 
      if to_price:
        dynamic_query_having.append("sum(r.nights*r.price) <= %s")
        params.append(to_price)
      if from_price:
        dynamic_query_having.append("sum(r.nights*r.price) >= %s")
        params.append(from_price)
      where_query = ' AND '.join(dynamic_query_where)
      haveing_query = ' AND '.join(dynamic_query_having)
      data = Reservation.searchin_reservation_info(where_query,haveing_query,hotel_id['hotel_id'],params)
      return JsonResponse({'data':data},status=200)
    except Exception as e:
      return erros.handel_errors(e,'/resrevation/views/get_filtered_rooms')
@csrf_exempt    
def get_specific_rooms(request):
    try:
      hotel_id = getattr(request,'hotel_id',None)
      reservation_ids = json.loads(request.body)
      return JsonResponse({'data':Reservation.get_specific_rooms(hotel_id['hotel_id'],reservation_ids['id'])},status=200)
    except Exception as e:
      return erros.handel_errors(e,'error/from/get_specific_rooms')
@csrf_exempt
def move_to_hotel(request,id):
  try:
     hotel_id = getattr(request,'hotel_id',None)
     Reservation.update_in_hotel(id,hotel_id['hotel_id'])
     return JsonResponse({'message':'in_hotel changed'},status=200)
  except Exception as e:
    return erros.handel_errors(e,'error/from/move_to_hotel')