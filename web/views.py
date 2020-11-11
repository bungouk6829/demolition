from django.shortcuts import render
from django.http import HttpResponse

def main(request):
	return render(request, 'web/main.html')

def menu_1(request, page):
	return render(request, 'web/menu_1.html', {'page':page})

def menu_2(request, page):
	return render(request, 'web/menu_2.html', {'page':page})

def menu_3(request, page):
	return render(request, 'web/menu_3.html', {'page':page})

def menu_4(request):
	return render(request, 'web/menu_4.html')

def menu_5(request):
	return render(request, 'web/menu_5.html')

def menu_6(request, page):
	return render(request, 'web/menu_6.html', {'page':page})
