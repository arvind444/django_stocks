from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Stocks
from .forms import Stocksform

# Create your views here.
def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']
		api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+ticker+'/quote?token=pk_d0d35da31224417eac8f9da0153874b2')

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error"

		return render(request, 'home.html', {'api' : api})

	else:
		return render(request, 'welcome.html', {})



def add_stocks(request):
	import requests
	import json

	if request.method == 'POST':
		form = Stocksform(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ("Stocks added successfully"))
			return redirect('add_stocks')
	else:
		ticker = Stocks.objects.all()
		output = []

		for ticker_item in ticker:
			api_request = requests.get('https://cloud.iexapis.com/stable/stock/'+str(ticker_item)+'/quote?token=pk_d0d35da31224417eac8f9da0153874b2')

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error"
				output = "Error"

		return render(request, 'add_stocks.html', {'ticker' : ticker, 'output' : output})

def delete(request, stocks_id):
	item = Stocks.objects.get(pk=stocks_id)
	item.delete()
	messages.success(request, ("Stocks deleted successfully"))
	return redirect('delete_stocks')

def delete_stocks(request):
	ticker = Stocks.objects.all()
	return render(request, 'delete_stocks.html', {'ticker' : ticker})