from django.urls import path
from .views import profile, signup, login, landing, logout, upload_profile_picture, select_catgory, play_quizz, quit_game
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/<int:user_id>', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('', landing, name='landing'),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('category/<int:user_id>', select_catgory, name='select_category'),
    path('session/<int:category_id>', play_quizz, name="session"),
    path('quit_game/<int:gamesession_id>', quit_game, name='quit_game'),
]



