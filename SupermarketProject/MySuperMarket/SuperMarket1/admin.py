from django.contrib import admin
from .models import MainCatogory, ProdCatogory, Products, CartItem

admin.site.register(MainCatogory)
admin.site.register(ProdCatogory)
admin.site.register(Products)
admin.site.register(CartItem)
