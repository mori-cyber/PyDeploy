from itertools import product

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    # path('products/', views.products, name="products"),
    # path('categories/', views.categories, name = "categories"),
    path('products/<int:product_id>', views.products, name="product")

]