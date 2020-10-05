 from django.db import models

# Create your models here.
class costomer(models.Model):
	name = models.CharField(max_length=100,null=True)
	phone = models.CharField(max_length=100,null=True)
	mail = models.CharField(max_length=100,null=True)
	d_created = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name
class tag(models.Model):
	name = models.CharField(max_length=100,null=True)
	def __str__(self):
		return self.name

class product(models.Model):
	category = (
		('Indoor', 'Indoor'),
		('Outdoor', 'Outdoor')
		)
	name = models.CharField(max_length=100,null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=100,null=True, choices=category)
	discription = models.CharField(max_length=100,null=True)
	d_created = models.DateTimeField(auto_now_add=True,null=True)
	tags = models.ManyToManyField(tag)
	def __str__(self):
		return self.name


class order(models.Model):
	status = (
		('pending', 'pending'),
		('out of stock', 'out of stock'),
		('Delivered', 'Delivered')
		)
	customer = models.ForeignKey(costomer, null=True, on_delete=models.SET_NULL)
	product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
	status = models.CharField(max_length=100,null=True, choices=status)
	d_created = models.DateTimeField(auto_now_add=True,null=True)
	def __str__(self):
		return self.product.name

