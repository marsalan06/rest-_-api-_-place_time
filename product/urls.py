from django.urls import path
from .import views
urlpatterns = [
    path('products/',views.Product_list),
    path('products/<int:pk>/',views.product_detail),
]