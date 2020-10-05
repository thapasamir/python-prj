import random
import string
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,'index.html')

def passwordgen(request):
	getnum = int(request.GET.get('str_count','default'))

	if type(getnum) == int:
		password = ''.join([random.choice(string.ascii_letters+string.digits+string.punctuation)for i in range(getnum)])
		reasult = {'lenth:':getnum,'password':password}
		return render(request,'pass.html',reasult)

	else:
		return HttpResponse('not done')