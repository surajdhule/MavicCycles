from django.contrib import admin
from .models import Cycle, Category, Description, Price
# Register your models here.


admin.site.register(Cycle)
admin.site.register(Category)
admin.site.register(Description)
admin.site.register(Price)
