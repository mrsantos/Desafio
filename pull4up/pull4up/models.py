from django.db import models

class Desafio(models.Model):
	purchaser_name = models.CharField(max_length=50)
	item_description  = models.CharField(max_length=80)
	item_price = models.FloatField()
	purchase_count = models.IntegerField()
	merchant_address = models.CharField(max_length=50)
	merchant_name = models.CharField(max_length=50)
