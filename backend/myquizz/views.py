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
from .utils import selected_question, display_question_choices


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
    

@never_cache
@login_required
def play_quizz(request, category_id):
    # Fetch User and Category
    user = request.user if request.user.is_authenticated else None
    category = get_object_or_404(Category, id=category_id)
    
    # Initiate or get Game Session
    gamesession, created = GameSession.objects.get_or_create(
        user=user,
        category=category,
        completed=False,
    )
    
    # Redirect To completed
    if gamesession.completed:
        return render(request, 'game/quiz_completed.html', {'score': gamesession.score})
    
    # Initialize session data if not already present
    if "questions" not in request.session:
        questions = selected_question(category_id)
        request.session['questions'] = questions
        request.session['current_index'] = 0
        
    questions = request.session['questions']
    current_index = request.session['current_index']
    
    # Check if All Question Has Been Answered
    if current_index >= len(questions):
        gamesession.mark_completed()
        del request.session['questions']
        del request.session['current_index']
        
        return render(request, "game/quiz_completed.html", {'score': gamesession.score})
    
    # Fetch the current question and it's choices
    question_id = questions[current_index]
    question = get_object_or_404(Question, id=question_id)
    choices = display_question_choices(question_id)
    
    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, id=selected_choice_id)
            if selected_choice.correct:
                gamesession.score += question.points
            request.session['current_index'] += 1
            gamesession.current_question = question
            gamesession.save()
            
        return redirect('session', category_id=category_id)
    
    return render(request, 'game/quiz_question.html', {
        'question': question,
        'choices': choices,
        'current_index': current_index + 1,
        'total_questions': len(questions),
    })
