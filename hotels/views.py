from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Hotels
from shared import erros


# Create your views here.
@csrf_exempt
def insert_in_hotel(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      email = data['email']
      password = data['password']
      name = data['name']
      address = data['address']
      hotel = Hotels(email=email,password=password,name=name,address=address)
      return JsonResponse(hotel.register_hotel(),status=200)
    except json.JSONDecodeError as e:
      return JsonResponse({'error':str(e),'from':'insert_in_hotel'},status=400)
    except erros.DataBaseErrors.ExecuteQuery as er:
      return JsonResponse({'error':str(er),'from':'insert_in_hotel'},status=401)
    except Exception as error:
      return JsonResponse({'error':str(error),'from':'insert_in_hotel'},status=400)
  else:
    return JsonResponse({'error':'httpmethod need to be post'},status=405)
  
def get_hotel(request):
  if request.method =='GET':
    try:
      hotel_id = getattr(request,'hotel_id',None)
      hotel = Hotels.get_hotel(hotel_id['hotel_id'])
      response_succses = JsonResponse({'hotel':hotel[0]},status=200)
      return response_succses
    except erros.DataBaseErrors.FormatingError as e:
      response = JsonResponse({'error':str(e),'from':'get_hotel'},status=400)
      return response
    except erros.DataBaseErrors.SelectOneError as seler:
      return JsonResponse({'error':str(seler),'from':'get_hotel'},status=400)
    except Exception as error:
      return JsonResponse({'error':str(error),'from':'get_hotel'},status=400)
  else:
    return JsonResponse({'eroor':'httpmethond need to be get'},status=405)
@csrf_exempt
def login_user(request):
  if request.method == 'POST':
    try:
      user = json.loads(request.body)
      return JsonResponse({'token':Hotels.login(user)},status=200)      
    except Exception as e:
      return JsonResponse({'error':str(e)},status=401)