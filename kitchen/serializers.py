from dataclasses import field
from rest_framework import serializers


from .models import Product, Dish, ProductsInDishes

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('product', 'price', 'deployer')
 
 
class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ('dish', 'products', 'type')
        