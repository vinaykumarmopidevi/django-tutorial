from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from .models import School

# Create your views here.
class IndexView(TemplateView):
    template_name="first_app/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["insert_me"] = "Django"
        return context


class SchoolListView(ListView):
    context_object_name='schools'
    model=School
    
class SchoolDetailView(DetailView):
    context_object_name="school_details"
    model=School
    template_name="first_app/school_detail.html"
