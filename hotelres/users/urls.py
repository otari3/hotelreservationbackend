from django.urls import path
from . import views
urlpatterns = [path('insert_user/',views.insert_user,name='insert_user') 
               ]