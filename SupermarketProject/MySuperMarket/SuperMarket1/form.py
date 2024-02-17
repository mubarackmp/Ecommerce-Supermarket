from django import forms
from .models import *


class MainCatForm(forms.ModelForm):
    class Meta:
        model = MainCatogory
        fields = '__all__'


class ProdCatForm(forms.ModelForm):
    class Meta:
        model = ProdCatogory
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'