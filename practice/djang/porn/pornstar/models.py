from django.db import models

# Create your models here.

class category(models.Model):
	cat = models.CharField(max_length=100,null=True)
	def __str__(self):
		return self.cat

class pornstar(models.Model):
	ss  = (('lado','lado'),
		('puti','puti')
		)
	name = models.CharField(max_length=100,null=True)
	size = models.FloatField(max_length=100,null=True)
	date = models.DateTimeField(auto_now_add=True,null=True)
	linga = models.CharField(max_length=100,null=True,choices=ss)
	char = models.ManyToManyField(category)
	def __str__(self):
		return self.name

class user(models.Model):
	name = models.CharField(max_length=50,null=True)
	email = models.CharField(max_length=50,null=True)
	def __str__(self):
		return self.name

class video_call(models.Model):
	qual = (('720p','720p'),
		    ('1080p','1080p'))
	user = models.ForeignKey(user,null=True, on_delete=models.SET_NULL)
	pornstar = models.ForeignKey(pornstar,null=True, on_delete=models.SET_NULL)
	quality = models.CharField(max_length=100,null=True,choices=qual)

