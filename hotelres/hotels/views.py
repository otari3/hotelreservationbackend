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
      name = data['name']
      address = data['address']
      hotel = Hotels(name=name,address=address)
      return JsonResponse(hotel.register_hotel(),status=200)
    except json.JSONDecodeError as e:
      return JsonResponse({'error':str(e),'from':'insert_in_hotel'},status=400)
    except erros.DataBaseErrors.ExecuteQuery as er:
      return JsonResponse({'error':str(er),'from':'insert_in_hotel'},status=400)
    except Exception as error:
      return JsonResponse({'error':str(error),'from':'insert_in_hotel'},status=400)
  else:
    return JsonResponse({'error':'httpmethod need to be post'},status=405)
  
def get_hotel(request,id):
  if request.method =='GET':
    try:
      hotel = Hotels.get_hotel(int(id))
      return JsonResponse({'hotel':hotel[0]},status=200)
    except erros.DataBaseErrors.FormatingError as e:
      response = JsonResponse({'error':str(e),'from':'get_hotel'},status=400)
      return response
    except erros.DataBaseErrors.SelectOneError as seler:
      return JsonResponse({'error':str(seler),'from':'get_hotel'},status=400)
    except Exception as error:
      return JsonResponse({'error':str(error),'from':'get_hotel'},status=400)
      
  else:
    return JsonResponse({'eroor':'httpmethond need to be get'},status=405)
      