from django.forms import ModelForm
from .models import Order,Product,Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
class ProductForm(ModelForm):
	class Meta:
		model=Product
		fields='__all__'
		exclude=['description','date_created','tags']
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']