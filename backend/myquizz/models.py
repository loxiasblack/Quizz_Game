from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


# User Class Extend from Django User (AbsrtactUser)
class CustomUser(AbstractUser):
    # choices
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        help_text='',  # Custom help text or remove it
    )
    MALE = 'male'
    FEMALE = 'female'
    CHOICES_SEXE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    # fields in database
    sexe = models.CharField(
        max_length=6,
        choices=CHOICES_SEXE,
        default=FEMALE
    )
    # Don't forget to handle the case of null attribute
    birth_date = models.DateField(auto_now=False, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username}"


# Category Class
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=150, blank=True)
    category_picture = models.ImageField(upload_to='category/')

    def __str__(self):
        return f"{self.name}"

# Define difficluty enumeration
class DifficultyLevel(models.TextChoices):
    EASY = 'Easy', 'Easy'
    MEDIUM = 'Medium', 'Medium'
    HARD = 'Hard', 'Hard'
    EXPERT = 'Expert', 'Expert'

# Question Class
class Question(models.Model):
    question = models.TextField(max_length=1500)
    difficulty = models.CharField(
        max_length=10,
        choices=DifficultyLevel.choices,
        default=DifficultyLevel.EASY,
    )
    points = models.PositiveIntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    descriptions = models.TextField(max_length=1500, blank=True)
    question_pictures = models.ImageField(upload_to='question/')

    def set_point_by_diffuculty(self):
        """ set the points based on the difficulty level. """
        diffuclty_points = {
            DifficultyLevel.EASY: 10,
            DifficultyLevel.MEDIUM: 20,
            DifficultyLevel.HARD: 30,
            DifficultyLevel.EXPERT: 40,
        }
        
        self.points = diffuclty_points.get(self.difficulty, 10)

    def save(self, *args, **kwargs):
        """ Autmatically set points based on difficulty before saving"""
        self.set_point_by_diffuculty()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.question}"


# Choice class
class Choice(models.Model):
    text = models.CharField(max_length=1000, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f'choice {"Correct" if self.correct else "Incorrect"}'


# GameSession Class to save the session in the database
class GameSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='gamesession')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='gamesession')
    current_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    
    def increment_score(self, points):
        """ update the score of the session"""
        self.score += points
        self.save()
    
    def mark_completed(self):
        """ mark the gamesession as completed"""
        self.completed = True
        self.ended_at = timezone.now()
        self.save()
    
    def __str__(self):
        return f"{self.user.username}'s Session on {self.category.name}"
