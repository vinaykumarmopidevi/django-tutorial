from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("signUp/",views.form_name_view,name="signUp"),
    path("product/",views.create_product,name="create_product")
   
]
