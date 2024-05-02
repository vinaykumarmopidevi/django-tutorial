from django.urls import path
from . import views

app_name='basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('deactivateUser/<slug:username>/', views.deactivateUser, name='deactivateUser'),
]
