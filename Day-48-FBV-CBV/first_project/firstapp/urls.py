from django.urls import path

from .views import CreateTopic,ListTopic,DetailTopic,UpdateTopic,DeleteTopic
#from .views import create_view,list_view,detail_view,update_view,delete_topic

urlpatterns = [
    
    #path("",create_view,name="create_view")
    path("create_view",CreateTopic.as_view(),name="create_view"),
    
    #path("",list_view,name="list_view")
    path("",ListTopic.as_view(),name="list_view"),
    
    #path("<int:pk>",detail_view,name="detail_view")
    path("<int:pk>/detail_view",DetailTopic.as_view(),name="detail_view"),
    
    #path("<int:pk>/update",update_view,name="update_view")
    path("<int:pk>/update",UpdateTopic.as_view(),name="update_view"),
    
    #path("<int:pk>/delete",delete_topic,name="delete_topic")
    path("<int:pk>/delete",DeleteTopic.as_view(),name="delete_topic")
]
