from django.urls import path
from . import views

app_name="first_app"
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('first_app/',views.SchoolListView.as_view(),name="list"),
    path('first_app/<int:pk>/',views.SchoolDetailView.as_view(),name="detail")
]
