from django.shortcuts import render
from . import forms
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    return render(request,"index.html")


def form_name_view(request):
    form=forms.FormName()

    if request.method=='POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Validation success')
            print(f'name: { form.cleaned_data['name']}')
            print(f'email: { form.cleaned_data['email']}')
            print(f'text: { form.cleaned_data['text']}')
        else:
            print('something wrong')

    return render(request,'form_page.html',{"form":form})