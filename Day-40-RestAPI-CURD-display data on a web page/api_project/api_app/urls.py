from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("blogPost/",views.BlogPostListCreate.as_view(),name="blogpost-view-create"),
    path("blogPost/<int:pk>",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name="update"
        )
]
