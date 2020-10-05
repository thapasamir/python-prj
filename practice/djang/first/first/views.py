from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,'index.html')

def capital(request):
	text = request.GET.get('text','default') 
	capital_check = request.GET.get('capital','off')
	count_check = request.GET.get('count','off')
	if capital_check == 'on':
		reas = text.upper()
		reasult ={'capital':'capitalized word is',
		'reasult':reas}
		#return HttpResponse('we are in capitalized')
		return render(request,'capital.html',reasult)
	elif count_check == 'on':
		reas = len(text)
		reasult_2 ={'count':'THere are',
		'reasult_two':reas}
		return render(request,'capital.html',reasult_2)

def download(request):
	return HttpResponse('i am in download <a href="http://127.0.0.1:8000/">back</a>')

