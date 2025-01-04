from .models import Question, Choice
from random import sample


def selected_question(category_id):
    DIFFICULTY_LEVELS = ['Easy', 'Medium', 'Hard', 'Expert']
    
    # Fetch the questions in the database
    
    selected_questions = []
    for difficulty in DIFFICULTY_LEVELS:
    
        questions_query = list(Question.objects.filter(category_id=category_id, difficulty=difficulty).values_list('id', flat=True))

        # check if there's more than 5 questions
        if len(questions_query) < 5:
            raise ValueError(f"Not enough questions available for the specified category and difficulty {difficulty}.")


        # select randomly 5 question
        selected_questions.extend(sample(questions_query, 5))
        
    return selected_questions
        

def display_question_choices(question_id):
    # select choices of the Question
    choices = list(Choice.objects.filter(question_id=question_id).values())
    if not choices:
        raise ValueError(f"No choices available for question ID {question_id}.")
    return choices
