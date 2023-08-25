from django.db import models


class Address(models.Model):
    line = models.CharField(max_length=250, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    item_name = models.CharField(max_length=50, blank=True, null=True)
    item_quantity = models.IntegerField(null=True, blank=True)
    item_price = models.FloatField(null=True, blank=True)

