# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class MainCatogory(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	
class ProdCatogory(models.Model):
	name = models.CharField(max_length=100)
	maincatogory = models.ForeignKey(MainCatogory, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
	
class Products(models.Model):
	name = models.CharField(max_length=100)
	prodcatogory = models.ForeignKey(ProdCatogory, on_delete=models.CASCADE)
	ptype = models.CharField(max_length=100,null=True)
	description = models.TextField(null=True)
	stock = models.PositiveIntegerField(default=0)
	mfd = models.DateField()
	exp = models.DateField()
	purchased_from_Company = models.CharField(max_length=100)
	Company_contact = models.IntegerField()
	purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='products/')
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class CartItem(models.Model):
	product = models.ForeignKey(Products, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		
		return f'{self.quantity} x {self.product.name}'
