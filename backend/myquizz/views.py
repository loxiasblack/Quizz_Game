from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from .forms import RegisterForms, LoginForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from .models import CustomUser, Question, Category, Choice, GameSession
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here. [never_cache] for blocking the browser caching
@never_cache
# Login to redirect to the Login page if the user is not connected
@login_required
def profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'game/profile.html', {'user' : user})


# Create a signup views
def signup(request):
    if request.method == 'POST':
        form = RegisterForms(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Registration successful!')
            return redirect('login')
    else:
        form = RegisterForms()
    return render(request, 'auth/signup.html', {'form': form})


# Login View
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('profile', user_id=user.id)
            else:
                messages.add_message(request, messages.WARNING, 'Invalid Username or Password')
                return redirect('login')
    else:
        form = LoginForm()
    
    return render(request, 'auth/login.html', { 'form': form })

#Logout View
def logout(request):
    if request.method == 'GET':
        auth_logout(request)
        return redirect('landing')

def landing(request):
    return render(request, 'game/home.html')

# Update picture Profile
@csrf_exempt
@login_required
def upload_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        try:
            profile_picture = request.FILES['profile_picture']
            
            user = request.user
            user.profile_picture = profile_picture
            user.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})



@never_cache
@login_required
def select_catgory(request, user_id):
    category = Category.objects.all().values()
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'game/category.html', {'user': user, 'categorys' : category})
    
