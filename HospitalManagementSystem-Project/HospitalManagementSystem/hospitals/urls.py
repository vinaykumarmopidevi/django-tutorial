from django.urls import path
from .views import *


urlpatterns = [
    path('',Index,name='index'),
    path('about/', About, name="about"),
    path('contact', contact, name='contact'),
    path('admin_home',  admin_home, name='admin_home'),
    
    path('login', admin_login, name='login'),
    path('logout',  Logout, name='logout'),
    
    path('add_doctor',  add_doctor, name='add_doctor'),
    path('edit_doctor/<int:pid>',edit_doctor,name='edit_doctor'),
    path('delete_doctor/<int:pid>',  delete_doctor, name='delete_doctor'),
    path('view_doctor',  view_doctor, name='view_doctor'),
    
    path('add_patient',  add_patient, name='add_patient'),
    path('edit_patient/<int:pid>',edit_patient,name='edit_patient'),
    path('delete_patient/<int:pid>', delete_patient, name='delete_patient'),
    path('view_patient', view_patient, name='view_patient'),
    
    
    
    path('add_appointment', add_appointment, name='add_appointment'),
    path('view_appointment', view_appointment, name='view_appointment'),
    path('delete_appointment/<int:pid>', delete_appointment, name='delete_appointment'),
    
    
    path('unread_queries', unread_queries, name='unread_queries'),
    path('read_queries', read_queries, name='read_queries'),
    path('view_queries/<int:pid>', view_queries, name='view_queries'),
    
]




