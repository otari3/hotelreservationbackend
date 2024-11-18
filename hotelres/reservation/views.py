from django.http import JsonResponse
from shared import erros
from django.views.decorators.csrf import csrf_exempt
from .models  import Reservation
import uuid
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
      dynamic_query_haveing = []
      dynamic_query_where = []
      #WHERE
      if check_in:
        dynamic_query_where.append(f" AND r.check_in > '{check_in}'" )
      if check_out:
        dynamic_query_where.append(f" AND 'r.check_out' < '{check_out}'")
      if reservation_id:
        dynamic_query_where.append(f" AND r.id > {reservation_id}")
      if search:
        dynamic_query_where.append(f" AND (u.name LIKE '%{search}%' OR u.personal_id LIKE '%{search}%')")
    ##HAVING 
      if to_price:
        dynamic_query_haveing.append(f" AND sum(r.nights*r.price) < {to_price}")
      if from_price:
        dynamic_query_haveing.append(f" AND sum(r.nights*r.price) > {from_price}")
      where_query = ''.join(dynamic_query_where)
      haveing_query = ''.join(dynamic_query_haveing)
      data = Reservation.searchin_reservation_info(where_query,haveing_query,hotel_id['hotel_id'])
      return JsonResponse({'data':data},status=200)
    except Exception as e:
      return erros.handel_errors(e,'/resrevation/views/get_filtered_rooms')