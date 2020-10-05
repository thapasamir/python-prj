from django.db import models

# Create your models here.

class sweet_fruits(models.Model):
	sta = (('raw','raw'),
			('rippen','rippen')
		 )
	name = models.CharField(max_length=100,null=True)
	price = models.CharField(max_length=100,null=True)
	status = models.CharField(max_length=100,null=False,choices=sta)

	def __str__(self):
		return self.name