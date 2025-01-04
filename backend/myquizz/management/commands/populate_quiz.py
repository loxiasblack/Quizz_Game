from django.core.management.base import BaseCommand
from myquizz.models import Category, Question, Choice


class Command(BaseCommand):
    help = 'Populates the database with quiz questions'
    
    def handle(self, *args, **options):
        math_category = Category.objects.get_or_create(
            name="Mathematic",
        )
        science_category = Category.objects.get_or_create(
            name="Science",
        )
        finance_category = Category.objects.get_or_create(
            name="Finance",
        )
        economy_category = Category.objects.get_or_create(
            name="Economy",
        )
        sport_category = Category.objects.get_or_create(
            name="Sport",
        )
        history_category = Category.objects.get_or_create(
            name="History",
        )
        
        math_data =  [
            {
                "question": "What is 15 + 27?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "42", "correct": True},
                    {"text": "32", "correct": False},
                    {"text": "52", "correct": False},
                    {"text": "44", "correct": False}
                ]
            },
            {
                "question": "Which number comes next in the sequence: 2, 4, 6, 8, ...?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "10", "correct": True},
                    {"text": "12", "correct": False},
                    {"text": "9", "correct": False},
                    {"text": "11", "correct": False}
                ]
            },
            {
                "question": "How many sides does a pentagon have?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "4", "correct": False},
                    {"text": "5", "correct": True},
                    {"text": "6", "correct": False},
                    {"text": "7", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": True},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "What is 8 × 7?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "54", "correct": False},
                    {"text": "56", "correct": True},
                    {"text": "58", "correct": False},
                    {"text": "60", "correct": False}
                ]
            },
            {
                "question": "Which fraction is equivalent to 1/2?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "2/6", "correct": False},
                    {"text": "3/4", "correct": False},
                    {"text": "2/4", "correct": True},
                    {"text": "3/5", "correct": False}
                ]
            },
            {
                "question": "What is 100 ÷ 4?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "20", "correct": False},
                    {"text": "25", "correct": True},
                    {"text": "30", "correct": False},
                    {"text": "35", "correct": False}
                ]
            },
            {
                "question": "Round 3.7 to the nearest whole number",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "3", "correct": False},
                    {"text": "4", "correct": True},
                    {"text": "3.5", "correct": False},
                    {"text": "3.8", "correct": False}
                ]
            },
            {
                "question": "What is the value of 5²?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "10", "correct": False},
                    {"text": "15", "correct": False},
                    {"text": "20", "correct": False},
                    {"text": "25", "correct": True}
                ]
            },
            {
                "question": "Which number is odd?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "2", "correct": False},
                    {"text": "4", "correct": False},
                    {"text": "6", "correct": False},
                    {"text": "9", "correct": True}
                ]
            },
            {
                "question": "What is 1/4 of 100?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "20", "correct": False},
                    {"text": "25", "correct": True},
                    {"text": "30", "correct": False},
                    {"text": "35", "correct": False}
                ]
            },
            {
                "question": "Find the missing angle in a triangle if two angles are 45° and 60°",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "65°", "correct": False},
                    {"text": "75°", "correct": True},
                    {"text": "85°", "correct": False},
                    {"text": "90°", "correct": False}
                ]
            },
            {
                "question": "Convert 0.125 to a fraction in lowest terms",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "1/6", "correct": False},
                    {"text": "1/8", "correct": True},
                    {"text": "1/4", "correct": False},
                    {"text": "1/5", "correct": False}
                ]
            },
            {
                "question": "What is the volume of a cube with side length 4?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "16", "correct": False},
                    {"text": "32", "correct": False},
                    {"text": "64", "correct": True},
                    {"text": "128", "correct": False}
                ]
            },
            {
                "question": "Solve: |x + 2| = 7",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "x = 5 or x = -9", "correct": True},
                    {"text": "x = 5 or x = 9", "correct": False},
                    {"text": "x = -5 or x = 9", "correct": False},
                    {"text": "x = -5 or x = -9", "correct": False}
                ]
            },
            {
                "question": "What is sin(30°)?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "1/4", "correct": False},
                    {"text": "1/3", "correct": False},
                    {"text": "1/2", "correct": True},
                    {"text": "2/3", "correct": False}
                ]
            },
            {
                "question": "Find the slope of the line passing through (2,3) and (4,7)",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "1", "correct": False},
                    {"text": "2", "correct": True},
                    {"text": "3", "correct": False},
                    {"text": "4", "correct": False}
                ]
            },
            {
                "question": "Simplify: √48",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "4√3", "correct": True},
                    {"text": "2√12", "correct": False},
                    {"text": "6√2", "correct": False},
                    {"text": "8√3", "correct": False}
                ]
            },
            {
                "question": "What is 2⁴?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "8", "correct": False},
                    {"text": "12", "correct": False},
                    {"text": "16", "correct": True},
                    {"text": "32", "correct": False}
                ]
            },
            {
                "question": "Find the median of: 3, 7, 8, 9, 11, 15",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "7", "correct": False},
                    {"text": "8.5", "correct": True},
                    {"text": "9", "correct": False},
                    {"text": "11", "correct": False}
                ]
            },
            {
                "question": "Solve: log₂(8)",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "2", "correct": False},
                    {"text": "3", "correct": True},
                    {"text": "4", "correct": False},
                    {"text": "6", "correct": False}
                ]
            },
            {
                "question": "What is the area of a circle with diameter 10? (Use π = 3.14)",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "78.5", "correct": True},
                    {"text": "31.4", "correct": False},
                    {"text": "157", "correct": False},
                    {"text": "314", "correct": False}
                ]
            },
            {
                "question": "Simplify: (2x + 3)(x - 1)",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "2x² + x - 3", "correct": True},
                    {"text": "2x² - 2x + 3", "correct": False},
                    {"text": "2x² + x + 3", "correct": False},
                    {"text": "2x² - x - 3", "correct": False}
                ]
            },
            {
                "question": "What is cos(60°)?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "1/4", "correct": False},
                    {"text": "1/3", "correct": False},
                    {"text": "1/2", "correct": True},
                    {"text": "2/3", "correct": False}
                ]
            },
            {
                "question": "Convert 5.67 × 10⁴ to standard form",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "567", "correct": False},
                    {"text": "5,670", "correct": False},
                    {"text": "56,700", "correct": True},
                    {"text": "567,000", "correct": False}
                ]
            },
            {
                "question": "Find the integral of x·ln(x)",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "x²/2·ln(x) - x²/4", "correct": True},
                    {"text": "x²/2·ln(x) - x²/2", "correct": False},
                    {"text": "x²·ln(x) - x²", "correct": False},
                    {"text": "x²/4·ln(x) - x²/4", "correct": False}
                ]
            },
            {
                "question": "What is the period of tan(x)?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "-π", "correct": False},
                    {"text": "π/2", "correct": False},
                    {"text": "π/4", "correct": False},
                    {"text": "π", "correct": True}
                ]
            },
            {
                "question": "Solve the system of equations: 3x + 2y = 7, 4x - y = 1",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "x = 1, y = 2", "correct": True},
                    {"text": "x = 2, y = 1", "correct": False},
                    {"text": "x = -1, y = 5", "correct": False},
                    {"text": "x = 3, y = -1", "correct": False}
                ]
            },
            {
                "question": "What is the sum of the series: 1 + 4 + 9 + 16 + ... + 100?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "385", "correct": True},
                    {"text": "395", "correct": False},
                    {"text": "405", "correct": False},
                    {"text": "415", "correct": False}
                ]
            },
            {
                "question": "Find the maximum value of f(x) = -x² + 6x - 5",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "4", "correct": True},
                    {"text": "5", "correct": False},
                    {"text": "6", "correct": False},
                    {"text": "7", "correct": False}
                ]
            },
            {
                "question": "Solve the differential equation: dy/dx = 2x",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "y = x² + C", "correct": True},
                    {"text": "y = 2x + C", "correct": False},
                    {"text": "y = x²/2 + C", "correct": False},
                    {"text": "y = 2x² + C", "correct": False}
                ]
            },
            {
                "question": "What is the volume of a sphere with radius 3?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "36π", "correct": True},
                    {"text": "28π", "correct": False},
                    {"text": "24π", "correct": False},
                    {"text": "12π", "correct": False}
                ]
            },
            {
                "question": "Find the eigenvalues of matrix [[3,1],[1,3]]",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "2 and 4", "correct": True},
                    {"text": "1 and 5", "correct": False},
                    {"text": "0 and 6", "correct": False},
                    {"text": "-1 and 7", "correct": False}
                ]
            },
            {
                "question": "What is the value of i⁴⁹?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "i", "correct": True},
                    {"text": "-i", "correct": False},
                    {"text": "1", "correct": False},
                    {"text": "-1", "correct": False}
                ]
            },
            {
                "question": "Find the area between y = x² and y = x from x = 0 to x = 1",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "1/6", "correct": False},
                    {"text": "1/3", "correct": True},
                    {"text": "1/2", "correct": False},
                    {"text": "2/3", "correct": False}
                ]
            },
            {
                "question": "What is the coefficient of x⁵y³ in (x + y)⁸?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "56", "correct": True},
                    {"text": "48", "correct": False},
                    {"text": "70", "correct": False},
                    {"text": "28", "correct": False}
                ]
            },
            {
                "question": "What is the degree of the minimal polynomial of √2 + √3 over ℚ?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "2", "correct": False},
                    {"text": "3", "correct": False},
                    {"text": "4", "correct": True},
                    {"text": "6", "correct": False}
                ]
            },
            {
                "question": "What is the fundamental group of S¹ × S¹?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "ℤ × ℤ", "correct": True},
                    {"text": "ℤ", "correct": False},
                    {"text": "ℤ₂", "correct": False},
                    {"text": "0", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": True},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "Calculate the Legendre symbol (7/23)",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "1", "correct": True},
                    {"text": "-1", "correct": False},
                    {"text": "0", "correct": False},
                    {"text": "undefined", "correct": False}
                ]
            },
            {
                "question": "Find the limit of (1 + z/n)^n as n → ∞ for complex z",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "e^z", "correct": True},
                    {"text": "ze^z", "correct": False},
                    {"text": "e^(z²)", "correct": False},
                    {"text": "undefined", "correct": False}
                ]
            },
            {
                "question": "Calculate the cohomology group H¹(RP², ℤ)",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "0", "correct": False},
                    {"text": "ℤ", "correct": False},
                    {"text": "ℤ₂", "correct": True},
                    {"text": "ℤ⊕ℤ", "correct": False}
                ]
            },
            {
                "question": "Find the radius of convergence of Σn²x^n",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "0", "correct": False},
                    {"text": "1/2", "correct": False},
                    {"text": "1", "correct": True},
                    {"text": "2", "correct": False}
                ]
            },
            {
                "question": "Solve the system: dx/dt = y, dy/dt = -sin(x)",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "E = y²/2 - cos(x) = constant", "correct": True},
                    {"text": "E = y²/2 + cos(x) = constant", "correct": False},
                    {"text": "E = y²/2 + sin(x) = constant", "correct": False},
                    {"text": "E = y²/2 - sin(x) = constant", "correct": False}
                ]
            },
            {
                "question": "What is the index of PSL(2,ℤ) in PSL(2,ℤ[1/p])?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "p + 1", "correct": True},
                    {"text": "p - 1", "correct": False},
                    {"text": "p", "correct": False},
                    {"text": "p²", "correct": False}
                ]
            },
            {
                "question": "Calculate the Lie bracket [X,Y] if X = ∂/∂x and Y = x∂/∂y",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "∂/∂y", "correct": True},
                    {"text": "-∂/∂y", "correct": False},
                    {"text": "x∂/∂y", "correct": False},
                    {"text": "0", "correct": False}
                ]
            },
            {
                "question": "Find the number of isomorphism classes of groups of order 8",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "3", "correct": False},
                    {"text": "4", "correct": False},
                    {"text": "5", "correct": True},
                    {"text": "6", "correct": False}
                ]
            },
            {
                "question": "What is the value of ζ(2)?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "π²/6", "correct": True},
                    {"text": "π²/4", "correct": False},
                    {"text": "π²/8", "correct": False},
                    {"text": "π²/3", "correct": False}
                ]
            },
        ]
        finance_data = [
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            {
                "question": "",
                "difficulty": "",
                "descriptions": "",
                "choices": [
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False},
                    {"text": "", "correct": False}
                ]
            },
            
        ]
        science_data = [
            
        ]
        history_data = [
            
        ]
        economy_data = [
            
        ]
        sport_data = [
            
        ]
        for q_data in math_data:
            # Create question
            question = Question.objects.create(
                question=q_data['question'],
                difficulty=q_data['difficulty'],
                category=math_category,
                descriptions=q_data['descriptions']
            )
            
            # Create choices for this question
            for choice in q_data['choices']:
                Choice.objects.create(
                    text=choice['text'],
                    question=question,
                    correct=choice['correct']
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created question: {question.question[:30]}...')
            )
        for q_data in science_data:
            # Create question
            question = Question.objects.create(
                question=q_data['question'],
                difficulty=q_data['difficulty'],
                category=science_category,
                descriptions=q_data['descriptions']
            )
            
            # Create choices for this question
            for choice in q_data['choices']:
                Choice.objects.create(
                    text=choice['text'],
                    question=question,
                    correct=choice['correct']
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created question: {question.question[:5]}...')
            )
        for q_data in finance_data:
            # Create question
            question = Question.objects.create(
                question=q_data['question'],
                difficulty=q_data['difficulty'],
                category=finance_category,
                descriptions=q_data['descriptions']
            )
            
            # Create choices for this question
            for choice in q_data['choices']:
                Choice.objects.create(
                    text=choice['text'],
                    question=question,
                    correct=choice['correct']
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created question: {question.question[:5]}...')
            )
        for q_data in history_data:
            # Create question
            question = Question.objects.create(
                question=q_data['question'],
                difficulty=q_data['difficulty'],
                category=history_data,
                descriptions=q_data['descriptions']
            )
            
            # Create choices for this question
            for choice in q_data['choices']:
                Choice.objects.create(
                    text=choice['text'],
                    question=question,
                    correct=choice['correct']
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created question: {question.question[:5]}...')
            )
        for q_data in economy_data:
            # Create question
            question = Question.objects.create(
                question=q_data['question'],
                difficulty=q_data['difficulty'],
                category=economy_category,
                descriptions=q_data['descriptions']
            )
            
            # Create choices for this question
            for choice in q_data['choices']:
                Choice.objects.create(
                    text=choice['text'],
                    question=question,
                    correct=choice['correct']
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created question: {question.question[:5]}...')
            )
        for q_data in sport_data:
            # Create question
            question = Question.objects.create(
                question=q_data['question'],
                difficulty=q_data['difficulty'],
                category=sport_data,
                descriptions=q_data['descriptions']
            )
            
            # Create choices for this question
            for choice in q_data['choices']:
                Choice.objects.create(
                    text=choice['text'],
                    question=question,
                    correct=choice['correct']
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created question: {question.question[:5]}...')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated quiz data')
        )
