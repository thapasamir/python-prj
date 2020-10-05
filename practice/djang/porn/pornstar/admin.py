from django.contrib import admin

# Register your models here.
from . models import pornstar,user,category,video_call
admin.site.register(user)
admin.site.register(pornstar)
admin.site.register(category)
admin.site.register(video_call)


