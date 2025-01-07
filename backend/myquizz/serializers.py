from rest_framework import serializers
from .models import Question, Choice, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'correct']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)  

    class Meta:
        model = Question
        fields = ['id', 'question', 'difficulty', 'points', 'category', 'descriptions', 'choices']
