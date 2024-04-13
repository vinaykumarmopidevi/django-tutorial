from django.urls import path
from . import views

urlpatterns = [
        path('',views.index,name='index'),
        path('products/', views.product_list, name="products"),
        path('users/', views.users, name="users"),
        path('empInfo/', views.emp_info, name="emp_info"),
        path('tableInfo/', views.table_info, name="table_info"),

]