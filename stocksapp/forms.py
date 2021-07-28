from django import forms 
from .models import Stocks

class Stocksform(forms.ModelForm):
	class Meta:
		model = Stocks
		fields = ['ticker']