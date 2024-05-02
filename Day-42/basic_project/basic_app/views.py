from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"basic_app/index.html")

@login_required
def user_logout(request):
    logout(request)
    
    return HttpResponseRedirect(reverse('basic_app:user_login'))

def register(request):
    registered = False
    
    if request.method== 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user=user_form.save()
            user.set_password(user.password)
            
            user.save()
            
            profile=profile_form.save(commit=False)
            
            
            profile.user=user
            
            if 'profile_pic' in request.FILES:
                print('fount it')
                profile.profile_pic=request.FILES['profile_pic']
                
                profile.save()
                registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    
    return render(request,"basic_app/registration.html",{
        
            'user_form':user_form,
            'profile_form':profile_form,
            'registered':registered
    })
    
def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                
                return HttpResponseRedirect(reverse('basic_app:dashboard'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details.")

    else:
        return render(request, 'basic_app/login.html', {})

@login_required(login_url="/basic_app/user_login/")
def dashboard(request):
    return render(request,"basic_app/dashboard.html")
        

@login_required
def deactivateUser(request, username):
    context = {}
    try:
        user = User.objects.get(username=username)
        if user.is_active:
            user.is_active = False
            user.save()
            context['msg'] = 'Profile successfully deactivated.'
        else:
            user.is_active = True
            user.save()
            context['msg'] = 'Profile successfully activated.'
    except user.DoesNotExist:
        context['msg'] = 'User does not exist.'
    except Exception as e:
        context['msg'] = e.message

    return render(request, 'basic_app/home.html', context=context)