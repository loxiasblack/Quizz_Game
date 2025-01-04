from django.contrib import admin
from .models import Question, Category, Choice, CustomUser
from .forms import QuestionAdminForm
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'category_picture']
    extra = 1

@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    fields = ['username', 'sexe', 'birth_date', 'profile_picture', 'email']

class ChoiceInline(admin.TabularInline):
    model = Choice

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ('question', 'category', 'difficulty', 'points')
    search_fields = ('question',)
    list_filter = ('category', 'difficulty')
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'correct')
    list_filter = ('question', 'correct')
    search_fields = ('text',)
