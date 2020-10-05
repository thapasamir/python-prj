from django.forms import ModelForm
from .models import *

class costumerform(ModelForm):
	class Meta:
		model = costomer
		fields = '__all__'