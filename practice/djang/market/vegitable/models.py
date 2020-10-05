from django.db import models

# Create your models here.
class vegitable(models.Model):
	vit =(('A','A'),
		  ('B','B'),
		  ('C','C'),
		  ('D','D'),
		)
	name = models.CharField(max_length=100,null=True)
	vitamin = models.CharField(max_length=100,null=True,choices=vit)
	price = models.FloatField(max_length=20,null=True)

	def __str__(self):
		return self.vitamin