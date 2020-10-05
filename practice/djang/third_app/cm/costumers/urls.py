from django.urls import path
from . import views


urlpatterns = [
	path('',views.home,name="home"),
	path('product/',views.produc_t,name="product"),
	path('costumers/<str:pk_test>/',views.costumers,name="costumers"),
	path('createorder/',views.createorder,name="createorder"),
	path('update_order/<str:pk>',views.updateorder,name="update_order"),
	path('delete/<str:pk>',views.delete,name="deletes")

]