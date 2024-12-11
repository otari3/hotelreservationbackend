from django.urls import path
from . import views

urlpatterns = [ path('get_report/<str:date>/',views.getting_report,name='get_report'),
               ]