from django.http import JsonResponse
from shared import erros
from .models import Report

def getting_report(request,date):
  hotel_id = getattr(request,'hotel_id',None)
  data = Report.get_report(date,hotel_id['hotel_id'])
  return JsonResponse({'data':list(data)},status =200)