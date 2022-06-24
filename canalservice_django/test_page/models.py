from django.db import models


class Numbers(models.Model):
    number = models.TextField(blank=True, null=True)
    order_number = models.TextField()
    price = models.TextField(blank=True, null=True)
    delivery_time = models.DateField(blank=True, null=True)
    price_in_rub = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numbers'