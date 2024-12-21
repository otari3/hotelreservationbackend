from django.urls import path
from . import views

urlpatterns = [ path('get_report/<str:date>/',views.getting_report,name='get_report'),
               path('dowloand_report/<str:date>/',views.generate_cv_report,name='generate_cv_report')
               ]