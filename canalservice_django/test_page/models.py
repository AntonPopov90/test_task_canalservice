from django.db import models

class GoogleSheet(models.Model):
    number = models.IntegerField()
    order_number = models.IntegerField()
    price = models.IntegerField()
    delivery_time = models.DateTimeField()
    price_in_rub = models.TextField()
