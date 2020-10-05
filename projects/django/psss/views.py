import random
import string
from django.http import HttpResponse
from django.shortcuts import render
def index(request): #rendering home page
	return render(request,'index.html')

def password(request):
	get_textfield = int(request.GET.get('input','default')) #getting the text of inputfield
	get_string = request.GET.get('str','off')
	get_number = request.GET.get('int','off')
	if  get_number == 'on' and get_string == 'on':
		final_password = ''.join([random.choice(string.ascii_letters+string.digits+string.punctuation)for i in range(get_textfield)])
		returning_fp ={'pas':final_password}
		return render(request,'reasult.html',returning_fp)
	if  get_number == 'off' and get_string == 'off':
		returning_fp ={'pas':"input is wrong please select what types of password do you want"}
		return render(request,'reasult.html',returning_fp)
	if  get_number == 'on' and get_string == 'off':
		final_password = ''.join([random.choice(string.digits+string.punctuation)for i in range(get_textfield)])
		returning_fp ={'pas':final_password}
		return render(request,'reasult.html',returning_fp)
	if  get_number == 'off' and get_string == 'on':
		final_password = ''.join([random.choice(string.ascii_letters+string.punctuation)for i in range(get_textfield)])
		returning_fp ={'pas':final_password}
		return render(request,'reasult.html',returning_fp)

	else:
		return HttpResponse('wrong')

