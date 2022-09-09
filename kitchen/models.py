from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    # создание таблицы продуктов
    product = models.CharField(max_length=200, unique=True, verbose_name='Товар')
    price = models.FloatField(validators=[MinValueValidator(0,0)], verbose_name='Цена')
    deployer = models.CharField(max_length=200, verbose_name='Поставщик')
        
    class Meta:
        ordering = ('product',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return self.product


class Dish(models.Model):
    # создание таблиц блюд
    dish = models.CharField(max_length=200, unique=True, verbose_name='Блюдо')
    products = models.ManyToManyField(Product, through='ProductsInDishes')
    type = models.CharField(max_length=200, verbose_name='Тип блюда')                       
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.dish


class ProductsInDishes(models.Model):
    # связующая таблица, в которй указываем кол-во продуктов
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    dish = models.ForeignKey(Dish, on_delete=models.DO_NOTHING)
    count = models.FloatField(validators=[MinValueValidator(0,0)], verbose_name='Кол-во')


class Menu(models.Model):
    # содание таблицы меню
    menu = models.CharField(max_length=200, unique=True, verbose_name='Меню')
    dishes = models.ManyToManyField(Dish) 