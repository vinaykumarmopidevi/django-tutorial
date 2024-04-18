from django.urls import path
from . import views

app_name="basic_app"
urlpatterns = [
    path("",views.index,name="index"),
    path("create_product/",views.create_product,name="create_product"),
    path("products/",views.products,name="product_list"),
    path("product_details/<int:pk>",views.product_details,name="product_details"),
    
    path("redirect_me/",views.redirect_me,name="redirect_me"),
    path("redirect_value/",views.redirect_value,name="redirect_value"),
]