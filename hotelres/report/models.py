from django.db import models
# Create your models here.

class Report(models.Model):
  check_in = models.DateField()
  check_out = models.DateField()
  user_name = models.TextField()
  user_personal_id = models.TextField()
  price = models.PositiveIntegerField()
  nights = models.PositiveIntegerField()
  hotel = models.UUIDField()
  room_number = models.TextField()
  @staticmethod
  def get_report(check_out,hotel_id):
    data = Report.objects.filter(check_out=check_out,  hotel=hotel_id)
    