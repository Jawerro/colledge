from django.contrib import admin

from .models import Product, Dish

class ProductInline(admin.TabularInline):
    model = Product
    extra = 7

class DishAdmin(admin.ModelAdmin):
    fields = ['name']
   


admin.site.register(Product)
admin.site.register(Dish, DishAdmin)