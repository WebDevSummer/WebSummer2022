from django.contrib import admin

# Register your models here.
from api1.models import NewProduct, NewCategories

admin.site.register(NewProduct)
admin.site.register(NewCategories)