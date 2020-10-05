from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *
from . forms import orderform

# Create your views here.
def home(request):
	c_ostumers = costomer.objects.all()
	o_rders = order.objects.all()
	total_order = o_rders.count()
	order_delivered =o_rders.filter(status='Delivered').count()
	order_pending = o_rders.filter(status='pending').count()
	dic ={'c_ostumers':c_ostumers,'o_rders':o_rders,'total_order':total_order,'order_delivered':order_delivered,'order_pending':order_pending}
	return render(request,'accounts/dashboard.html',dic)


	
def produc_t(request):
	p_roduct = product.objects.all()
	return render(request,'accounts/products.html',{'p_roduct':p_roduct})



def costumers(request,pk_test):
	alu = costomer.objects.get(id=pk_test)
	bhalu = alu.order_set.all()
	order_count = bhalu.count()
	contex = {'alu':alu,'bhalu':bhalu,'order_count':order_count}
	return render(request,'accounts/costumers.html',contex)

def createorder(request):
	form = orderform()
	if request.method == 'POST':
		form = orderform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	contex = {'form':form}
	return render(request,'accounts/form_st.html',contex)

def updateorder(request, pk):
	Order = order.objects.get(id=pk)
	form = orderform(instance=Order)
	if request.method == 'POST':
		form = orderform(request.POST, instance=Order)
		if form.is_valid():
			form.save()
			return redirect('/')

	contex ={'form':form}
	return render(request,'accounts/form_st.html',contex)

def delete(request,pk):
	item = order.objects.get(id=pk)
	if request.method == "POST":
		item.delete()
		return redirect('/')
	contex = {'item':item}
	return render(request,'accounts/del.html',contex)
