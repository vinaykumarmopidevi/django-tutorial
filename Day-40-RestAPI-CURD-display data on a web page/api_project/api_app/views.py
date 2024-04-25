from django.shortcuts import render
from rest_framework import generics,status
from .models import BlogPost
from .serializers import BlogPostSerializer
import requests
from rest_framework.response import Response


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    
    
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    lookup_field="pk"
    
    
    
def index(request):
    response=requests.get("http://127.0.0.1:8000/blogPost/")
    posts=response.json()
    print(posts)
    return render(request,"index.html",{"posts":posts})