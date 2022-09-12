from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from rest_framework import viewsets

from .models import Product, Dish
from .forms import DishForm
from .serializers import ProductSerializer, DishSerializer


def index(request):
    return render(request, 'main/index.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('product')
    serializer_class = ProductSerializer


class ProductEditView(generic.UpdateView):
    model = Product
    template_name = 'main/products/edit_product.html'
    fields = '__all__'
    success_url = reverse_lazy('kitchen:table_products')


class DishEditView(generic.UpdateView):
    model = Dish
    template_name = 'main/products/edit_dish.html'
    fields = '__all__'
    success_url = reverse_lazy('kitchen:table_dishes')


class ProductView(generic.ListView):
    model = Product
    template_name = 'main/products/table_products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class DishView(generic.ListView):
    model = Dish
    template_name = 'main/dishes/table_dishes.html'
    context_object_name = 'dishes'
    queryset = Dish.objects.all()


class  ProductAddView(generic.CreateView):
    model = Product
    template_name = 'main/products/add_product.html'
    fields = ['product', 'price', 'deployer'] 
    success_url = reverse_lazy('kitchen:table_products')


class  DishAddView(generic.CreateView):
    model = DishForm
    fields = '__all__'
    template_name = 'main/dishes/add_dish.html'
    success_url = reverse_lazy('kitchen:table_dishes')   


class ProductDeleteView(generic.DeleteView, SuccessMessageMixin):
    model = Product
    success_message = 'Продукт удален'
    success_url = reverse_lazy('kitchen:table_products')


class DishDeleteView(generic.DeleteView, SuccessMessageMixin):
    model = Dish
    success_message = 'Блюдо удалено'
    success_url = reverse_lazy('kitchen:table_dishes')
