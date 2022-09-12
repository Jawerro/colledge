from django.urls import path
from rest_framework import routers


from . import views
from .views import ProductView, ProductAddView, ProductEditView,  ProductDeleteView, ProductViewSet
from .views import  DishView, DishAddView, DishEditView, DishDeleteView

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
urlpatterns = router.urls



# app_name = 'kitchen'
# urlpatterns = [
#     path('', views.index, name = 'index'),
#     path('products', ProductView.as_view(), name = 'table_products'),
#     path('products\<int:pk>\edit', ProductEditView.as_view(), name = 'edit_product'),
#     path('products\add', ProductAddView.as_view(), name = 'add_product'),
#     path('products\<int:pk>\delete', ProductDeleteView.as_view(), name = 'delete_product'),
#     path('dishes', DishView.as_view(), name='table_dishes'),
#     path('dishes\add', DishAddView.as_view(), name = 'add_dish'),
#     path('dishes\<int:pk>\edit', DishEditView.as_view(), name = 'edit_dish'),
#     path('dishes\<int:pk>\delete', DishDeleteView.as_view(), name = 'delete_product'),
#     ]