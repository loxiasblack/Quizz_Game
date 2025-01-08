from django.urls import path, include
from .views import profile, signup, login, landing, logout, upload_profile_picture, select_catgory, play_quizz, quit_game, QuestionViewSet, ChoiceViewSet, Top_ranking
from django.contrib.auth import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('profile/<int:user_id>', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', landing, name='landing'),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('category/<int:user_id>', select_catgory, name='select_category'),
    path('session/<int:category_id>', play_quizz, name="session"),
    path('quit_game/<int:gamesession_id>', quit_game, name='quit_game'),
    path('top_ranking/', Top_ranking, name="top_ranking"),
]



