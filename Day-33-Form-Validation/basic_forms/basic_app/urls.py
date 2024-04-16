from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("form_page/",views.form_name_view,name="form_name_view")
]
