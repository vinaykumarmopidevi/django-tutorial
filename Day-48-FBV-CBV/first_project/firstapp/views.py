from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .forms import TopicForm
from .models import Topic
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
"""
def create_view(request):
    form=TopicForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,"create_view.html",context={"form":form})
"""

class CreateTopic(CreateView):
    model=Topic
    form_class = TopicForm
    

"""
def list_view(request):
    data=Topic.objects.all()
    return render(request,"list_view.html",context={"data":data})
"""
class ListTopic(ListView):
    model=Topic


"""
def detail_view(request, id):
    data = Topic.objects.get(id = id)
    return render(request, "detail_view.html", context={"data":data})
"""


class DetailTopic(DetailView):
    model=Topic
    
"""
def update_view(request,pk):
    obj=get_object_or_404(Topic,id=pk)
    form=TopicForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        
    return render(request,"update_view.html",context={"form":form})
"""
class UpdateTopic(UpdateView):
    model=Topic
    form_class=TopicForm
    success_url="/"

"""
def delete_topic(request,pk):
    
    data=Topic.objects.get(id=pk)
    data.delete()
    return redirect("list_view")
"""
class DeleteTopic(DeleteView):
    model=Topic
    success_url=reverse_lazy('list_view')
    