from django.contrib import admin

# Register your models here.
from .models import order,costomer,product,tag
admin.site.register(costomer)
admin.site.register(product)
admin.site.register(order)
admin.site.register(tag)

