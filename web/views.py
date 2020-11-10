from django.shortcuts import render
from django.http import HttpResponse

def main(request):
	return render(request, 'web/main.html')

def introduction(request):
	return render(request, 'web/introduction.html')

def history(request):
	return render(request, 'web/history.html')

def map(request):
	return render(request, 'web/map.html')
