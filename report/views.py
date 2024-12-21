from django.http import JsonResponse,HttpResponse
from shared import erros
from .models import Report
from django.views.decorators.csrf import csrf_exempt
import csv
def getting_report(request,date):
  hotel_id = getattr(request,'hotel_id',None)
  data = Report.get_report(date,hotel_id['hotel_id'])
  return JsonResponse({'data':list(data)},status =200)
@csrf_exempt
def generate_cv_report(request,date):
  hotel_id = getattr(request,'hotel_id',None)
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = f'attachment; filename="test_report.csv"'
  writer = csv.writer(response)
  writer.writerow(['Guest Name', 'Guest Id','Room Number','Check In','Check Out','Nights','Price'])
  data = Report.get_report(date,hotel_id['hotel_id'])
  if data.exists:
    sumOfPrice = 0
    for item in data:
      writer.writerow([item['user_name'], item['user_personal_id'],item['room_number'],item['check_in'],item['check_out'],item['nights'],item['price']])
      sumOfPrice+=item['price']
    writer.writerow(['', '','','','','',sumOfPrice])
  else:
    raise('there is no report for this date')
  return response