import os
from django.core.management.base import BaseCommand
from django.core.files import File
from myquizz.models import Category, Question, Choice


class Command(BaseCommand):
    help = 'Populates the database with quiz questions'
    
    def handle(self, *args, **options):
        # declare the path for the image
        math_image_path = 'media/category/mathematic.jpg'
        
        science_image_path = 'media/category/science.jpeg'
        economy_image_path = 'media/category/economics.jpg'
        finance_image_path = 'media/category/finance.jpg'
        sport_image_path = 'media/category/Sport.jpg'
        history_image_path = 'media/category/history.jpg'
        
        math_category, created =  Category.objects.get_or_create(
            name="Mathematic",
        )
        science_category, created = Category.objects.get_or_create(
            name="Science",
        )
        finance_category, created = Category.objects.get_or_create(
            name="Finance",
        )
        economy_category, created = Category.objects.get_or_create(
            name="Economy",
        )
        sport_category, created = Category.objects.get_or_create(
            name="Sport",
        )
        history_category, created = Category.objects.get_or_create(
            name="History",
        )
        
        
        
        # Assign the image to the category_picture field
        if os.path.exists(math_image_path):
            with open(math_image_path, 'rb') as f:
                math_category.category_picture.save(
                    os.path.basename(math_image_path),  # Save the file with the same name
                    File(f),  # Pass the file object
                    save=True  # Save the instance
                )
            print(f"Image assigned to '{math_category.name}' category.")
        else:
            print(f"Image not found at {math_image_path}. Skipping image assignment.")
            
        if os.path.exists(science_image_path):
            with open(science_image_path, 'rb') as f:
                science_category.category_picture.save(
                    os.path.basename(science_image_path),  # Save the file with the same name
                    File(f),  # Pass the file object
                    save=True  # Save the instance
                )
            print(f"Image assigned to '{science_category.name}' category.")
        else:
            print(f"Image not found at {science_image_path}. Skipping image assignment.")
            
        if os.path.exists(economy_image_path):
            with open(economy_image_path, 'rb') as f:
                economy_category.category_picture.save(
                    os.path.basename(economy_image_path),  # Save the file with the same name
                    File(f),  # Pass the file object
                    save=True  # Save the instance
                )
            print(f"Image assigned to '{economy_category.name}' category.")
        else:
            print(f"Image not found at {economy_image_path}. Skipping image assignment.")

        if os.path.exists(finance_image_path):
            with open(finance_image_path, 'rb') as f:
                finance_category.category_picture.save(
                    os.path.basename(finance_image_path),  # Save the file with the same name
                    File(f),  # Pass the file object
                    save=True  # Save the instance
                )
            print(f"Image assigned to '{finance_category.name}' category.")
        else:
            print(f"Image not found at {finance_image_path}. Skipping image assignment.")

        if os.path.exists(history_image_path):
            with open(history_image_path, 'rb') as f:
                history_category.category_picture.save(
                    os.path.basename(history_image_path),  # Save the file with the same name
                    File(f),  # Pass the file object
                    save=True  # Save the instance
                )
            print(f"Image assigned to '{history_category.name}' category.")
        else:
            print(f"Image not found at {history_image_path}. Skipping image assignment.")

        if os.path.exists(sport_image_path):
            with open(sport_image_path, 'rb') as f:
                sport_category.category_picture.save(
                    os.path.basename(sport_image_path),  # Save the file with the same name
                    File(f),  # Pass the file object
                    save=True  # Save the instance
                )
            print(f"Image assigned to '{sport_category.name}' category.")
        else:
            print(f"Image not found at {sport_image_path}. Skipping image assignment.")
        
        
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
                "question": "What is the primary purpose of a savings account?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "To invest in stocks", "correct": False},
                    {"text": "To safely store money while earning interest", "correct": True},
                    {"text": "To pay bills", "correct": False},
                    {"text": "To get loans", "correct": False}
                ]
            },
            {
                "question": "What does ATM stand for?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Automatic Transfer Machine", "correct": False},
                    {"text": "Automated Teller Machine", "correct": True},
                    {"text": "Automatic Trading Method", "correct": False},
                    {"text": "Automated Time Management", "correct": False}
                ]
            },
            {
                "question": "Which of these is a form of debt?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Stocks", "correct": False},
                    {"text": "Credit card balance", "correct": True},
                    {"text": "Savings account", "correct": False},
                    {"text": "Cash", "correct": False}
                ]
            },
            {
                "question": "What is a budget?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "A type of investment", "correct": False},
                    {"text": "A bank account", "correct": False},
                    {"text": "A plan for managing", "correct": True},
                    {"text": "A type of loan", "correct": False}
                ]
            },
            {
                "question": "What is interest",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "A type of stock", "correct": False},
                    {"text": "Money paid for using borrowed money", "correct": True},
                    {"text": "A bank fee", "correct": False},
                    {"text": "A type of tax", "correct": False}
                ]
            },
            {
                "question": "Which of these is typically the most liquid asset?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "House", "correct": False},
                    {"text": "Car", "correct": False},
                    {"text": "Cash", "correct": True},
                    {"text": "Jewelry", "correct": False}
                ]
            },
            {
                "question": "What is income?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Money spent on goods", "correct": False},
                    {"text": "Money received from work or investments", "correct": True},
                    {"text": "Money owed to others", "correct": False},
                    {"text": "Money in savings", "correct": False}
                ]
            },
            {
                "question": "What is a deposit?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "A withdrawal of money", "correct": False},
                    {"text": "A loan from a bank", "correct": False},
                    {"text": "Money placed into an account", "correct": True},
                    {"text": "A type of credit card", "correct": False}
                ]
            },
            {
                "question": "What does FICO measure?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Stock prices", "correct": False},
                    {"text": "Interest rates", "correct": False},
                    {"text": "Credit score", "correct": True},
                    {"text": "Inflation rate", "correct": False}
                ]
            },
            {
                "question": "What is a debit card?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "A card that builds credit", "correct": False},
                    {"text": "A card that directly accesses your bank account", "correct": True},
                    {"text": "A type of credit card", "correct": False},
                    {"text": "A store loyalty card", "correct": False}
                ]
            },
            {
                "question": "What is compound interest?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Interest earned only on principal", "correct": False},
                    {"text": "Interest earned on both principal and accumulated interest", "correct": True},
                    {"text": "A fixed interest rate", "correct": True},
                    {"text": "A type of loan interest", "correct": False}
                ]
            },
            {
                "question": "What is diversification in investing?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Buying only one type of stock", "correct": False},
                    {"text": "Spreading investments across different assets", "correct": True},
                    {"text": "Investing in real estate only", "correct": False},
                    {"text": "Keeping all money in cash", "correct": False}
                ]
            },
            {
                "question": "What is a mutual fund?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "A type of savings account", "correct": False},
                    {"text": "A pool of money invested in various securities", "correct": True},
                    {"text": "A government bond", "correct": False},
                    {"text": "A type of credit card", "correct": False}
                ]
            },
            {
                "question": "What is an emergency fund typically recommended to cover?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "1-2 weeks of expenses", "correct": False},
                    {"text": "1 month of expenses", "correct": False},
                    {"text": "3-6 months of expenses", "correct": True},
                    {"text": "2 years of expenses", "correct": False}
                ]
            },
            {
                "question": "What is a bond",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "A type of stock", "correct": False},
                    {"text": "A loan to a company or government", "correct": True},
                    {"text": "A savings account", "correct": False},
                    {"text": "A type of insurance", "correct": False}
                ]
            },
            {
                "question": "What is inflation?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Rising stock prices", "correct": False},
                    {"text": "Rising interest rates", "correct": False},
                    {"text": "General increase in prices over time", "correct": True},
                    {"text": "Increase in savings", "correct": False}
                ]
            },
            {
                "question": "What is a dividend?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "A type of loan", "correct": False},
                    {"text": "A company's distribution of profits to shareholders", "correct": True},
                    {"text": "A bank fee", "correct": False},
                    {"text": "An interest payment", "correct": False}
                ]
            },
            {
                "question": "What is an IRA ?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "A type of loan", "correct": False},
                    {"text": "A retirement account", "correct": True},
                    {"text": "A checking score", "correct": False},
                    {"text": "A credit score", "correct": False}
                ]
            },
            {
                "question": "What is net worth?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Total income", "correct": False},
                    {"text": "Total assets minus total liabilities", "correct": True},
                    {"text": "Total savings", "correct": False},
                    {"text": "Total investments", "correct": False}
                ]
            },
            {
                "question": "What is a bear market?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "A market with rising prices", "correct": False},
                    {"text": "A market with falling prices", "correct": True},
                    {"text": "A stable market", "correct": False},
                    {"text": "A new market", "correct": False}
                ]
            },
            {
                "question": "What is the Rule of 72?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "A tax regulation", "correct": False},
                    {"text": "A formula to estimate investment doubling time", "correct": True},
                    {"text": "A retirement rule", "correct": False},
                    {"text": "A lending principle", "correct": False}
                ]
            },
            {
                "question": "What is a P/E ratio?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Price to earnings ratio", "correct": True},
                    {"text": "Profit to expense ratio", "correct": False},
                    {"text": "Payment to equity ratio", "correct": False},
                    {"text": "Principal to interest ratio", "correct": False}
                ]
            },
            {
                "question": "What is short selling?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Quick trading", "correct": False},
                    {"text": "Selling borrowed shares hoping price will fall", "correct": True},
                    {"text": "Selling at a loss", "correct": False},
                    {"text": "Selling small amounts", "correct": False}
                ]
            },
            {
                "question": "What is beta in investing?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "A measure of volatility relative to market", "correct": True},
                    {"text": "A type of stock", "correct": False},
                    {"text": "An interst rate", "correct": False},
                    {"text": "A trading strategy", "correct": False}
                ]
            },
            {
                "question": "What is a derivative?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "A type of stock", "correct": False},
                    {"text": "A financial instrument based on underlying assets", "correct": True},
                    {"text": "A bank account", "correct": False},
                    {"text": "A type of loan", "correct": False}
                ]
            },
            {
                "question": "What is arbitrage?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "A type of stock trading", "correct": False},
                    {"text": "Profiting from price differences in different markets", "correct": True},
                    {"text": "Long-term investing", "correct": False},
                    {"text": "Risk management", "correct": False}
                ]
            },
            {
                "question": "What is EBITDA?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "A type of stock", "correct": False},
                    {"text": "Earnings before interest, taxes, depreciation, and amortization", "correct": True},
                    {"text": "A market index", "correct": False},
                    {"text": "A trading strategy", "correct": False}
                ]
            },
            {
                "question": "What is a callable bond?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "A bond that can be redeemed early by issuer", "correct": True},
                    {"text": "A bond that pays regular interest", "correct": False},
                    {"text": "A government bond", "correct": False},
                    {"text": "A corporate bond", "correct": False}
                ]
            },
            {
                "question": "What is duration in bond investing?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Time until maturity", "correct": False},
                    {"text": "Measure of price sensitivty to interest rate changes", "correct": True},
                    {"text": "Length of interest payments", "correct": False},
                    {"text": "Bond rating period", "correct": False}
                ]
            },
            {
                "question": "What is a zero-coupon bond?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "A worthless bond", "correct": False},
                    {"text": "A bond sold at discount with no interest payments", "correct": True},
                    {"text": "A government bon", "correct": False},
                    {"text": "A high-yield bond", "correct": False}
                ]
            },
            {
                "question": "What is the Black-Scholes model used for?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Stock valuation", "correct": False},
                    {"text": "Options pricing", "correct": True},
                    {"text": "Bond pricing", "correct": False},
                    {"text": "Real estate valuation", "correct": False}
                ]
            },
            {
                "question": "What is a butterfly spread?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "A type of stock strategy", "correct": False},
                    {"text": "An options strategy combining four different options", "correct": True},
                    {"text": "A futures contract", "correct": False},
                    {"text": "A forex strategy", "correct": False}
                ]
            },
            {
                "question": "What is delta hedging?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "A type of insurance", "correct": False},
                    {"text": "Neutralizing portfolio sensitivity to price changes", "correct": True},
                    {"text": "A trading strategy", "correct": False},
                    {"text": "Risk management technique", "correct": False}
                ]
            },
            {
                "question": "What is a swap in derivatives?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Exchange of stocks", "correct": False},
                    {"text": "Exchange of future cash flows", "correct": True},
                    {"text": "Exchange of bonds", "correct": False},
                    {"text": "Exchange of commodities", "correct": False}
                ]
            },
            {
                "question": "What is a Monte Carlo simulation in finance?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "A gambling strategy", "correct": False},
                    {"text": "A trading system", "correct": False},
                    {"text": "A valuation method", "correct": False},
                    {"text": "A probability-based modeling technique", "correct": True}
                ]
            },
            {
                "question": "What is the Treynor ratio?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Market volatility measure", "correct": False},
                    {"text": "Price-to-earnings ratio", "correct": False},
                    {"text": "Return per unit of systematic risk", "correct": True},
                    {"text": "Dividend yield measure", "correct": False}
                ]
            },
            {
                "question": "What is duration convexity?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Second-order measure of interest rate risk", "correct": True},
                    {"text": "Bond maturity measure", "correct": False},
                    {"text": "Stock price volatility", "correct": False},
                    {"text": "Option pricing factor", "correct": False}
                ]
            },
            {
                "question": "What is a swaption?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "A type of stock option", "correct": False},
                    {"text": "A futures contract", "correct": False},
                    {"text": "A bond option", "correct": False},
                    {"text": "An option on a swap agreement", "correct": True}
                ]
            },
            {
                "question": "What is the Girsanov theorem used for?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Stock valuation", "correct": False},
                    {"text": "Change of probability measure in option pricing", "correct": True},
                    {"text": "Bond pricing", "correct": False},
                    {"text": "Portfolio optimization", "correct": False}
                ]
            },
            {
                "question": "What is a quanto option?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "A regular option", "correct": False},
                    {"text": "A futures option", "correct": False},
                    {"text": "A stock option", "correct": False},
                    {"text": "An option with foreign exchange rate protection ", "correct": True}
                ]
            },
            
        ]
        science_data = [
            {
                "question": "What is the closest planet to the Sun?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Venus", "correct": False},
                    {"text": "Mars", "correct": False},
                    {"text": "Mercury", "correct": True},
                    {"text": "Earth", "correct": False}
                ]
            },
            {
                "question": "What is the chemical symbol for water?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Wa", "correct": False},
                    {"text": "H2O", "correct": True},
                    {"text": "O2", "correct": False},
                    {"text": "CO2", "correct": False}
                ]
            },
            {
                "question": "What is the largest organ in the human body?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Heart", "correct": False},
                    {"text": "Brain", "correct": False},
                    {"text": "Liver", "correct": False},
                    {"text": "Skin", "correct": True}
                ]
            },

            {
                "question": "Which of these is a renewable energy source?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Coal", "correct": False},
                    {"text": "Solar power", "correct": True},
                    {"text": "Natural gas", "correct": False},
                    {"text": "Oil", "correct": False}
                ]
            },
            {
                "question": "What is photosynthesis?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Light reflection", "correct": False},
                    {"text": "Process of plants making food using sunlight", "correct": True},
                    {"text": "Cell division", "correct": False},
                    {"text": "Water evaporation", "correct": False}
                ]
            },
            {
                "question": "How many bones are in the human body?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "156", "correct": False},
                    {"text": "186", "correct": False},
                    {"text": "206", "correct": True},
                    {"text": "226", "correct": False}
                ]
            },
            {
                "question": "What is the hardest natural substance on Earth?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Gold", "correct": False},
                    {"text": "Iron", "correct": False},
                    {"text": "Diamond", "correct": True},
                    {"text": "Platinum", "correct": False}
                ]
            },
            {
                "question": "What makes up most of Earth's atmosphere?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Oxygen", "correct": False},
                    {"text": "Carbon dioxide", "correct": False},
                    {"text": "Nitrogen", "correct": True},
                    {"text": "Hydrogen", "correct": False}
                ]
            },
            {
                "question": "What is the speed of light?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "299,792 kilometers per second", "correct": True},
                    {"text": "199,792 kilometers per second", "correct": False},
                    {"text": "399,792 kilometers per second", "correct": False},
                    {"text": "499,792 kilometers per second", "correct": False}
                ]
            },
            {
                "question": "Which blood type is known as the universal donor?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Type A", "correct": False},
                    {"text": "Type B", "correct": False},
                    {"text": "Type AB", "correct": False},
                    {"text": "Type O", "correct": True}
                ]
            },
            {
                "question": "What is the Doppler effect?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Change in wave frequency due to relative motion", "correct": True},
                    {"text": "Light reflection", "correct": False},
                    {"text": "Magnetic field effect", "correct": False},
                    {"text": "Gravitational force", "correct": False}
                ]
            },
            {
                "question": "What is the unit of electrical resistance?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Volt", "correct": False},
                    {"text": "Ampere", "correct": False},
                    {"text": "Ohm", "correct": True},
                    {"text": "Watt", "correct": False}
                ]
            },
            {
                "question": "Which element has the atomic number 6?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Oxygen", "correct": False},
                    {"text": "Carbon", "correct": True},
                    {"text": "Nitrogen", "correct": False},
                    {"text": "Helium", "correct": False}
                ]
            },
            {
                "question": "Which planet has the most moons?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Mars", "correct": False},
                    {"text": "Jupiter", "correct": True},
                    {"text": "Saturn", "correct": False},
                    {"text": "Uranus", "correct": False}
                ]
            },
            {
                "question": "What is mitosis?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Cell death", "correct": False},
                    {"text": "Cell division creating identical cells", "correct": True},
                    {"text": "Protein synthesis", "correct": False},
                    {"text": "Energy production", "correct": False}
                ]
            },
            {
                "question": "What is the main function of red blood cells?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Fight infection", "correct": False},
                    {"text": "Carry oxygen", "correct": True},
                    {"text": "Clot blood", "correct": False},
                    {"text": "Produce antibodies", "correct": False}
                ]
            },
            {
                "question": "What is the chemical formula for table salt?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "NaCl", "correct": True},
                    {"text": "H2O", "correct": False},
                    {"text": "CO2", "correct": False},
                    {"text": "CaCO3", "correct": False}
                ]
            },
            {
                "question": "What is absolute zero in Celsius?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "-273.15°C ", "correct": True},
                    {"text": "-300°C", "correct": False},
                    {"text": "-250°C", "correct": False},
                    {"text": "-200°C", "correct": False}
                ]
            },
            {
                "question": "What type of radiation has the longest wavelength?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Gamma rays", "correct": False},
                    {"text": "X-rays", "correct": False},
                    {"text": "Ultraviolet", "correct": False},
                    {"text": "Radio waves", "correct": True}
                ]
            },
            {
                "question": "What is the process of radioactive decay called?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Fusion", "correct": False},
                    {"text": "Fission", "correct": False},
                    {"text": "Half-life", "correct": True},
                    {"text": "Nuclear synthesis", "correct": False}
                ]
            },
            {
                "question": "What is Heisenberg's Uncertainty Principle?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Theory of relativity", "correct": False},
                    {"text": "Cannot simultaneously know position and momentum precisely", "correct": True},
                    {"text": "Law of gravity", "correct": False},
                    {"text": "Conservation of energy", "correct": False}
                ]
            },
            {
                "question": "What is the Krebs cycle?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Water cycle", "correct": False},
                    {"text": "Cellular energy production cycle", "correct": True},
                    {"text": "Carbon cycle", "correct": False},
                    {"text": "Nitrogen cycle", "correct": False}
                ]
            },
            {
                "question": "What is the strong nuclear force?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Electromagnetic force", "correct": False},
                    {"text": "Force holding atomic nuclei together", "correct": True},
                    {"text": "Gravitational force", "correct": False},
                    {"text": "Weak nuclear force", "correct": False}
                ]
            },
            {
                "question": "What is a quaternary structure in proteins?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Primary amino acid sequence", "correct": False},
                    {"text": "Multiple protein subunit arrangement", "correct": True},
                    {"text": "Alpha helix formation", "correct": False},
                    {"text": "Beta sheet structure", "correct": False}
                ]
            },
            {
                "question": "What is Bernoulli's principle?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Force of gravity", "correct": False},
                    {"text": "Increase in fluid speed decreases pressure", "correct": True},
                    {"text": "Magnetic field effect", "correct": False},
                    {"text": "Electric current flow", "correct": False}
                ]
            },
            {
                "question": "What is dark matter?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Black holes", "correct": False},
                    {"text": "Invisible matter affecting gravity", "correct": True},
                    {"text": "Space dust", "correct": False},
                    {"text": "Dead stars", "correct": False}
                ]
            },
            {
                "question": "What is a chirality in chemistry?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Chemical reaction", "correct": False},
                    {"text": "Atomic structure", "correct": False},
                    {"text": "Molecular handedness", "correct": True},
                    {"text": "Bond type", "correct": False}
                ]
            },
            {
                "question": "What is quantum entanglement?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Atomic fusion", "correct": False},
                    {"text": "Particles remain connected regardless of distance", "correct": True},
                    {"text": "Nuclear fission", "correct": False},
                    {"text": "Electron configuration", "correct": False}
                ]
            },
            {
                "question": "What is the function of telomeres?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Cell division", "correct": False},
                    {"text": "Protein synthesis", "correct": False},
                    {"text": "Energy production", "correct": False},
                    {"text": "Protect chromosome ends", "correct": True}
                ]
            },
            {
                "question": "What is a Bose-Einstein condensate?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "New element", "correct": False},
                    {"text": "Chemical compound", "correct": False},
                    {"text": "Matter state at extremely low temperature", "correct": True},
                    {"text": "Nuclear reaction", "correct": False}
                ]
            },
            {
                "question": "What is the Casimir effect?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Gravitational force", "correct": False},
                    {"text": "Quantum mechanical attraction between plates in vacuum", "correct": True},
                    {"text": "Magnetic effect", "correct": False},
                    {"text": "Electric field", "correct": False}
                ]
            },
            {
                "question": "What is Maxwell's demon paradox?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Time travel theory", "correct": False},
                    {"text": "Quantum mechanics principle", "correct": False},
                    {"text": "Relativity paradox", "correct": False},
                    {"text": "Violation of second law of thermodynamics thought experiment", "correct": True}
                ]
            },
            {
                "question": "What is a topological quantum computer?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Standard computer", "correct": False},
                    {"text": "Supercomputer", "correct": False},
                    {"text": "Computer using quantum braiding", "correct": True},
                    {"text": "Neural network", "correct": False}
                ]
            },
            {
                "question": "What is the holographic principle?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "3D imaging", "correct": False},
                    {"text": "Information content of space encoded on boundary", "correct": True},
                    {"text": "Light reflection", "correct": False},
                    {"text": "Quantum states", "correct": False}
                ]
            },
            {
                "question": "What is loop quantum gravity?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "String theory", "correct": False},
                    {"text": "Dark matter theory", "correct": False},
                    {"text": "Universe expansion theory", "correct": False},
                    {"text": "Theory combining quantum mechanics and gravity", "correct": True}
                ]
            },
            {
                "question": "What is supersymmetry?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Crystal structure", "correct": False},
                    {"text": "heoretical symmetry between fermions and bosons", "correct": True},
                    {"text": "Atomic symmetry", "correct": False},
                    {"text": "Molecular symmetry", "correct": False}
                ]
            },
            {
                "question": "What is decoherence in quantum mechanics?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Wave function", "correct": False},
                    {"text": "Particle spin", "correct": False},
                    {"text": "Energy level", "correct": False},
                    {"text": "Loss of quantum behavior through environment interaction", "correct": True}
                ]
            },
            {
                "question": "What is the AdS/CFT correspondence?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Mathematical equation", "correct": False},
                    {"text": "Duality between string theory and quantum field theory", "correct": True},
                    {"text": "Chemical bond", "correct": False},
                    {"text": "Physical constant", "correct": False}
                ]
            },
            {
                "question": "What is a Yang-Mills theory?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Gravity theory", "correct": False},
                    {"text": "Gauge field theory", "correct": True},
                    {"text": "Quantum theory", "correct": False},
                    {"text": "Relativity theory", "correct": False}
                ]
            },
            {
                "question": "What is the Wheeler-DeWitt equation?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Chemical equation", "correct": False},
                    {"text": "Mathematical formula", "correct": False},
                    {"text": "Physical law", "correct": False},
                    {"text": "Quantum description of universe", "correct": True}
                ]
            },
        ]
        history_data = [
            {
                "question": "Who wrote the Declaration of Independence?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "George Washington", "correct": False},
                    {"text": "Benjamin Franklin", "correct": False},
                    {"text": "Thomas Jefferson", "correct": True},
                    {"text": "John Adams", "correct": False}
                ]
            },
            {
                "question": "In which year did World War II end?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "1943", "correct": False},
                    {"text": "1944", "correct": False},
                    {"text": "1945", "correct": True},
                    {"text": "1946", "correct": False}
                ]
            },
            {
                "question": "Who was the first President of the United States?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Thomas Jefferson", "correct": False},
                    {"text": "John Adams", "correct": False},
                    {"text": "Benjamin Franklin", "correct": False},
                    {"text": "George Washington", "correct": True}
                ]
            },
            {
                "question": "Which ancient civilization built the pyramids?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Greeks", "correct": False},
                    {"text": "Romans", "correct": False},
                    {"text": "Egyptians", "correct": True},
                    {"text": "Persians", "correct": False}
                ]
            },
            {
                "question": "What event started World War I?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Pearl Harbor attack", "correct": False},
                    {"text": "Assassination of Archduke Franz Ferdinand", "correct": True},
                    {"text": "German invasion of Poland", "correct": False},
                    {"text": "Russian Revolution", "correct": False}
                ]
            },
            {
                "question": "Who was the first woman to win a Nobel Prize?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Mother Teresa", "correct": False},
                    {"text": "Jane Addams", "correct": False},
                    {"text": "Pearl Buck", "correct": False},
                    {"text": "Marie Curie", "correct": True}
                ]
            },
            {
                "question": "What year did Christopher Columbus first reach the Americas?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "1482", "correct": False},
                    {"text": "1492", "correct": True},
                    {"text": "1502", "correct": False},
                    {"text": "1512", "correct": False}
                ]
            },
            {
                "question": "Which empire was ruled by Julius Caesar?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Greek", "correct": False},
                    {"text": "Persian", "correct": False},
                    {"text": "Roman", "correct": True},
                    {"text": "Ottoman", "correct": False}
                ]
            },
            {
                "question": "What was the name of the first successful English colony in America?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Plymouth", "correct": False},
                    {"text": "Jamestown", "correct": True},
                    {"text": "Roanoke", "correct": False},
                    {"text": "Massachusetts Bay", "correct": False}
                ]
            },
            {
                "question": "Who painted the Mona Lisa?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Vincent van Gogh", "correct": False},
                    {"text": "Pablo Picasso", "correct": False},
                    {"text": "Leonardo da Vinci", "correct": True},
                    {"text": "Michelangelo", "correct": False}
                ]
            },
            {
                "question": "Which treaty ended World War I?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Treaty of Paris", "correct": False},
                    {"text": "Treaty of London", "correct": False},
                    {"text": "Treaty of Versailles", "correct": True},
                    {"text": "Treaty of Vienna", "correct": False}
                ]
            },
            {
                "question": "Who was the leader of the Soviet Union during the Cuban Missile Crisis?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Joseph Stalin", "correct": False},
                    {"text": "Nikita Khrushchev", "correct": True},
                    {"text": "Vladimir Lenin", "correct": False},
                    {"text": "Leon Trotsky", "correct": False}
                ]
            },
            {
                "question": "What was the name of the ancient trade route connecting China with Europe?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Spice Route", "correct": False},
                    {"text": "Tea Trail", "correct": False},
                    {"text": "Gold Path", "correct": False},
                    {"text": "Silk Road", "correct": True}
                ]
            },
            {
                "question": "Who wrote \"The Communist Manifesto\"?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Marx and Engels", "correct": True},
                    {"text": "Lenin and Trotsky", "correct": False},
                    {"text": "Stalin and Marx", "correct": False},
                    {"text": "Engels and Lenin", "correct": False}
                ]
            },
            {
                "question": "During which period did the Renaissance begin?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "12th century", "correct": False},
                    {"text": "16th century", "correct": False},
                    {"text": "14th century", "correct": True},
                    {"text": "18th century", "correct": False}
                ]
            },
            {
                "question": "What was the capital of the Byzantine Empire?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Rome", "correct": False},
                    {"text": "Athens", "correct": False},
                    {"text": " Constantinople", "correct": True},
                    {"text": "Alexandria", "correct": False}
                ]
            },
            {
                "question": "Which civilization developed the first system of writing?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Egyptians", "correct": False},
                    {"text": "Sumerians", "correct": True},
                    {"text": "Chinese", "correct": False},
                    {"text": "Indians", "correct": False}
                ]
            },
            {
                "question": "Who was the first Emperor of China?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Sun Yat-sen", "correct": False},
                    {"text": "Qin Shi Huang", "correct": True},
                    {"text": "Kublai Khan", "correct": False},
                    {"text": "Han Wudi", "correct": False}
                ]
            },
            {
                "question": "What was the main cause of the French Revolution?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Social inequality and financial crisis", "correct": True},
                    {"text": "Foreign invasion", "correct": False},
                    {"text": "Religious conflict", "correct": False},
                    {"text": "Natural disasters", "correct": False}
                ]
            },
            {
                "question": "Which battle ended the American Revolution?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Battle of Bunker Hill", "correct": False},
                    {"text": "Battle of Yorktown", "correct": True},
                    {"text": "Battle of Saratoga", "correct": False},
                    {"text": "Battle of Trenton", "correct": False}
                ]
            },
            {
                "question": "What was the name of Genghis Khan's grandson who founded the Yuan Dynasty?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Ögedei Khan", "correct": False},
                    {"text": "Möngke Khan", "correct": False},
                    {"text": "Güyük Khan", "correct": False},
                    {"text": "Kublai Khan", "correct": True}
                ]
            },
            {
                "question": "During which dynasty was the Great Wall of China primarily built?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Ming Dynasty", "correct": True},
                    {"text": "Han Dynasty", "correct": False},
                    {"text": "Tang Dynasty", "correct": False},
                    {"text": "Song Dynasty", "correct": False}
                ]
            },
            {
                "question": "Who was the last Ptolemaic ruler of Egypt?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Nefertiti", "correct": False},
                    {"text": "Cleopatra VII", "correct": True},
                    {"text": "Hatshepsut", "correct": False},
                    {"text": "Arsinoe II", "correct": False}
                ]
            },
            {
                "question": "What was the significance of the Peace of Westphalia?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Ended the Crusades", "correct": False},
                    {"text": "United Italy", "correct": False},
                    {"text": "Established principle of state sovereignty", "correct": True},
                    {"text": "Created the Holy Roman Empire", "correct": False}
                ]
            },
            {
                "question": "Which empire controlled the Spice Trade in the Indian Ocean before European arrival?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Arab Caliphate", "correct": True},
                    {"text": "Persian Empire", "correct": False},
                    {"text": "Mongol Empire", "correct": False},
                    {"text": "Chinese Empire", "correct": False}
                ]
            },
            {
                "question": "What was the main cause of the Bronze Age collapse?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Natural disasters", "correct": False},
                    {"text": "Multiple systems collapse", "correct": True},
                    {"text": "Foreign invasion", "correct": False},
                    {"text": "Disease outbreak", "correct": False}
                ]
            },
            {
                "question": "Who wrote the \"Wealth of Nations\"?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "John Locke", "correct": False},
                    {"text": "Adam Smith", "correct": True},
                    {"text": "Thomas Hobbes", "correct": False},
                    {"text": "Jean-Jacques Rousseau", "correct": False}
                ]
            },
            {
                "question": "What was the primary purpose of the Council of Trent?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Counter the Protestant Reformation", "correct": True},
                    {"text": "Launch the Crusades", "correct": False},
                    {"text": "Elect a new Pope", "correct": False},
                    {"text": "Establish the Eastern Orthodox Church", "correct": False}
                ]
            },
            {
                "question": "Which civilization first developed the concept of zero?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Greeks", "correct": False},
                    {"text": "Maya", "correct": True},
                    {"text": "Romans", "correct": False},
                    {"text": "Persians", "correct": False}
                ]
            },
            {
                "question": "What was the purpose of the Rosetta Stone?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Religious text", "correct": False},
                    {"text": "Ancient calendar", "correct": False},
                    {"text": "Royal decree", "correct": False},
                    {"text": "Translation tool for Egyptian hieroglyphs", "correct": True}
                ]
            },
            {
                "question": "What was the significance of the Battle of Kadesh?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Earliest documented battle with tactical details", "correct": True},
                    {"text": "First recorded peace treaty", "correct": False},
                    {"text": "Rise of the Assyrian Empire", "correct": False},
                    {"text": "Fall of the Hittite Empire", "correct": False}
                ]
            },
            {
                "question": "Who was Ashoka the Great's grandfather?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Bindusara", "correct": False},
                    {"text": "Chandragupta Maurya", "correct": True},
                    {"text": "Bimbisara", "correct": False},
                    {"text": "Ajatashatru", "correct": False}
                ]
            },
            {
                "question": "What was the primary cause of the Antonine Plague?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Bacteria", "correct": False},
                    {"text": "Parasites", "correct": False},
                    {"text": "Smallpox virus", "correct": True},
                    {"text": "Fungal infection", "correct": False}
                ]
            },
            {
                "question": "Which Chinese philosophy emphasized the \"Rectification of Names\"?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Taoism", "correct": False},
                    {"text": "Confucianism", "correct": True},
                    {"text": "Legalism", "correct": False},
                    {"text": "Mohism", "correct": False}
                ]
            },
            {
                "question": "What was the purpose of the Ancient Egyptian \"Texts of the Pyramids\"?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Historical records", "correct": False},
                    {"text": "Agricultural guides", "correct": False},
                    {"text": "Funerary texts for pharaohs", "correct": True},
                    {"text": "Mathematical treatises", "correct": False}
                ]
            },
            {
                "question": "What was the significance of the Battle of Talas?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Fall of the Persian Empire", "correct": False},
                    {"text": "Rise of the Mongol Empire", "correct": False},
                    {"text": "Spread of paper-making to Islamic world", "correct": True},
                    {"text": "End of the Tang Dynasty", "correct": False}
                ]
            },
            {
                "question": "Who wrote the \"Arthashastra\"?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Ashoka", "correct": False},
                    {"text": "Kalidasa", "correct": False},
                    {"text": "Patanjali", "correct": False},
                    {"text": "Kautilya", "correct": True}
                ]
            },
            {
                "question": "What was the significance of the Battle of Ain Jalut?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "First defeat of Mongol army", "correct": True},
                    {"text": "End of the Crusades", "correct": False},
                    {"text": "Fall of Jerusalem", "correct": False},
                    {"text": "Rise of the Ottoman Empire", "correct": False}
                ]
            },
            {
                "question": "What was the main cause of the Late Bronze Age systems collapse?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Climate change", "correct": False},
                    {"text": "Foreign invasion", "correct": False},
                    {"text": "Economic crisis", "correct": False},
                    {"text": "Multiple interconnected causes", "correct": True}
                ]
            },
            {
                "question": "What was the purpose of the Ancient Mesopotamian Kudurru stones?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Religious artifacts", "correct": False},
                    {"text": "Royal genealogies", "correct": False},
                    {"text": "Land grant documentation", "correct": True},
                    {"text": "Astronomical calculations",  "correct": False}
                ]
            },
        ]
        economy_data = [
            {
                "question": "What is economics?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "The study of money only", "correct": False},
                    {"text": "The study of business", "correct": False},
                    {"text": "The study of stock markets", "correct": False},
                    {"text": "The study of how society manages scarce resources", "correct": True}
                ]
            },
            {
                "question": "What is supply?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "The desire to purchase goods", "correct": False},
                    {"text": "The amount of a product available for sale", "correct": True},
                    {"text": "The price of goods", "correct": False},
                    {"text": "The number of consumers", "correct": False}
                ]
            },
            {
                "question": "What is demand?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "The quantity of a good producers want to sell", "correct": False},
                    {"text": "The amount buyers are willing and able to purchase", "correct": True},
                    {"text": "The total supply in a market", "correct": False},
                    {"text": "The current price of a good", "correct": False}
                ]
            },
            {
                "question": "What happens to price when demand increases but supply stays the same?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Price increases", "correct": True},
                    {"text": "Price decreases", "correct": False},
                    {"text": "Price stays the same", "correct": False},
                    {"text": "Price disappears", "correct": False}
                ]
            },
            {
                "question": "What is a market?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Only retail stores", "correct": False},
                    {"text": "Only online shopping", "correct": False},
                    {"text": "Only a physical place to buy goods", "correct": False},
                    {"text": "Where buyers and sellers interact", "correct": True}
                ]
            },
            {
                "question": "What is GDP?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Government Domestic Policy", "correct": False},
                    {"text": "Global Development Plan", "correct": False},
                    {"text": "General Domestic Price", "correct": False},
                    {"text": "Gross Domestic Product ", "correct": True}
                ]
            },
            {
                "question": "What is inflation?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "When prices rise over time", "correct": True},
                    {"text": "When unemployment rises", "correct": False},
                    {"text": "When prices fall", "correct": False},
                    {"text": "When trade increases", "correct": False}
                ]
            },
            {
                "question": "What is scarcity?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "When something is expensive", "correct": False},
                    {"text": "When unlimited wants exceed limited resources", "correct": True},
                    {"text": "When something is rare", "correct": False},
                    {"text": "When something is popular", "correct": False}
                ]
            },
            {
                "question": "What is a monopoly?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "A board game", "correct": False},
                    {"text": "Multiple sellers in a market", "correct": False},
                    {"text": "A single seller in a market", "correct": True},
                    {"text": "A type of tax", "correct": False}
                ]
            },
            {
                "question": "What are goods?",
                "difficulty": "Easy",
                "descriptions": "",
                "choices": [
                    {"text": "Only services provided", "correct": False},
                    {"text": "Only luxury items", "correct": False},
                    {"text": "Only necessary items", "correct": False},
                    {"text": "Physical items that satisfy wants or needs", "correct": True}
                ]
            },
            {
                "question": "What is perfect competition?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "When one company dominates", "correct": False},
                    {"text": "Many sellers, homogeneous products, perfect information", "correct": True},
                    {"text": "Government regulation", "correct": False},
                    {"text": "International trade", "correct": False}
                ]
            },
            {
                "question": "What is a public good?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Any government service", "correct": False},
                    {"text": "Any shared resource", "correct": False},
                    {"text": "Any free product", "correct": False},
                    {"text": "Non-rivalrous and non-excludable good ", "correct": True}
                ]
            },
            {
                "question": "What is monetary policy?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Government spending", "correct": False},
                    {"text": "Central bank's management of money supply and interest rates", "correct": True},
                    {"text": "Tax policy", "correct": False},
                    {"text": "Trade policy", "correct": False}
                ]
            },
            {
                "question": "What is elasticity of demand?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "How flexible a product is", "correct": False},
                    {"text": "How supply changes", "correct": False},
                    {"text": "How demand responds to price changes", "correct": True},
                    {"text": "How fast goods sell", "correct": False}
                ]
            },
            {
                "question": "What is a market failure?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Business bankruptcy", "correct": False},
                    {"text": "When markets don't allocate resources efficiently", "correct": True},
                    {"text": "Stock market crash", "correct": False},
                    {"text": "Bank failure", "correct": False}
                ]
            },
            {
                "question": "What is comparative advantage?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Ability to produce at lower opportunity cost", "correct": True},
                    {"text": "Having more resources", "correct": False},
                    {"text": "Being bigger than competitors", "correct": False},
                    {"text": "Having better technology", "correct": False}
                ]
            },
            {
                "question": "What is fiscal policy?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Government spending and taxation decisions", "correct": True},
                    {"text": "International trade rules", "correct": False},
                    {"text": "Business regulations", "correct": False},
                    {"text": "Central bank monetary actions", "correct": False}
                ]
            },
            {
                "question": "What is the law of diminishing returns?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Decreasing prices over time", "correct": False},
                    {"text": "Reduced demand over time", "correct": False},
                    {"text": "Falling profits", "correct": False},
                    {"text": "Additional inputs eventually yield smaller increases in output", "correct": True}
                ]
            },
            {
                "question": "What is opportunity cost?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "The value of the next best alternative given up", "correct": True},
                    {"text": "The monetary cost of something", "correct": False},
                    {"text": "The cost of production", "correct": False},
                    {"text": "The selling price", "correct": False}
                ]
            },
            {
                "question": "What is a recession?",
                "difficulty": "Medium",
                "descriptions": "",
                "choices": [
                    {"text": "Rising inflation only", "correct": False},
                    {"text": "Rising unemployment only", "correct": False},
                    {"text": "Two consecutive quarters of declining GDP", "correct": True},
                    {"text": "Period of rising GDP", "correct": False}
                ]
            },
            {
                "question": "What is the Phillips Curve?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Supply and demand curve", "correct": False},
                    {"text": "GDP growth curve", "correct": False},
                    {"text": "Population growth curve", "correct": False},
                    {"text": "Relationship between inflation and unemployment", "correct": True}
                ]
            },
            {
                "question": "What is the Nash equilibrium?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Market price equilibrium", "correct": False},
                    {"text": "Trade balance", "correct": False},
                    {"text": "No player can benefit by changing strategy unilaterally", "correct": True},
                    {"text": "Budget balance", "correct": False}
                ]
            },
            {
                "question": "What is the Ricardian equivalence?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Trade theory", "correct": False},
                    {"text": "Government deficit financing doesn't affect aggregate demand", "correct": True},
                    {"text": "Price theory", "correct": False},
                    {"text": "Money supply theory", "correct": False}
                ]
            },
            {
                "question": "What is the Gini coefficient?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Economic growth measure", "correct": False},
                    {"text": "Measure of income inequality", "correct": True},
                    {"text": "Population density measure", "correct": False},
                    {"text": "Trade balance measure", "correct": False}
                ]
            },
            {
                "question": "What is the efficient market hypothesis?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Asset prices reflect all available information", "correct": True},
                    {"text": "Government regulation theory", "correct": False},
                    {"text": "Production efficiency theory", "correct": False},
                    {"text": "Labor market theory", "correct": False}
                ]
            },
            {
                "question": "What is moral hazard?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Environmental damage", "correct": False},
                    {"text": "Increased risk-taking due to protection from consequences", "correct": True},
                    {"text": "Unethical business practices", "correct": False},
                    {"text": "False advertising", "correct": False}
                ]
            },
            {
                "question": "What is the multiplier effect?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Population growth", "correct": False},
                    {"text": "Initial change in spending leads to larger change in GDP", "correct": True},
                    {"text": "Compound interest", "correct": False},
                    {"text": "Price inflation", "correct": False}
                ]
            },
            {
                "question": "What is the Coase theorem?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Theory of inflation", "correct": False},
                    {"text": "Efficient outcome regardless of initial property rights with no transaction costs", "correct": True},
                    {"text": "Theory of employment", "correct": False},
                    {"text": "Theory of trade", "correct": False}
                ]
            },
            {
                "question": "What is the IS-LM model?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Model of macroeconomic equilibrium in goods and money markets", "correct": True},
                    {"text": "International trade model", "correct": False},
                    {"text": "Supply chain model", "correct": False},
                    {"text": "Labor market model", "correct": False}
                ]
            },
            {
                "question": "What is adverse selection?",
                "difficulty": "Hard",
                "descriptions": "",
                "choices": [
                    {"text": "Poor hiring practices", "correct": False},
                    {"text": "Bad investment choices", "correct": False},
                    {"text": "Product defects", "correct": False},
                    {"text": "Market inefficiency due to information asymmetry", "correct": True}
                ]
            },
            {
                "question": "What is the Mundell-Fleming model?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "IS-LM model for open economies", "correct": True},
                    {"text": "Labor market model", "correct": False},
                    {"text": "Growth model", "correct": False},
                    {"text": "Trade theory", "correct": False}
                ]
            },
            {
                "question": "What is the Heckscher-Ohlin model?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Labor market theory", "correct": False},
                    {"text": "Growth theory", "correct": False},
                    {"text": "International trade based on factor endowments", "correct": True},
                    {"text": "Money supply theory", "correct": False}
                ]
            },
            {
                "question": "What is the Lucas critique?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Growth theory criticism", "correct": False},
                    {"text": "Trade theory criticism", "correct": False},
                    {"text": "Economic policy effects cannot be predicted from historical data", "correct": True},
                    {"text": "Market efficiency criticism", "correct": False}
                ]
            },
            {
                "question": "What is the Overlapping Generations Model?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Population model", "correct": False},
                    {"text": "Dynamic economic model with different age cohorts", "correct": True},
                    {"text": "Trade model", "correct": False},
                    {"text": "Labor market model", "correct": False}
                ]
            },
            {
                "question": "What is the Real Business Cycle theory?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Market cycle theory", "correct": False},
                    {"text": "Economic fluctuations from real shocks rather than monetary factors", "correct": True},
                    {"text": "Trade cycle theory", "correct": False},
                    {"text": "Employment cycle theory", "correct": False}
                ]
            },
            {
                "question": "What is the Calvo pricing model?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": " Market pricing theory", "correct": False},
                    {"text": "Staggered price adjustment model in New Keynesian economics", "correct": True},
                    {"text": "International pricing theory", "correct": False},
                    {"text": "Resource pricing theory", "correct": False}
                ]
            },
            {
                "question": "What is the Arrow-Debreu model?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Trade model", "correct": False},
                    {"text": "Labor market model", "correct": False},
                    {"text": "Growth model", "correct": False},
                    {"text": "General equilibrium model with complete markets", "correct": True}
                ]
            },
            {
                "question": "What is the Stolper-Samuelson theorem?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Trade protection affects factor returns", "correct": True},
                    {"text": "Growth theory", "correct": False},
                    {"text": "Price theory", "correct": False},
                    {"text": "Labor theory", "correct": False}
                ]
            },
            {
                "question": "What is the Solow growth model?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Population growth model", "correct": False},
                    {"text": "Long-run economic growth model with technology and capital accumulation", "correct": True},
                    {"text": "Trade model", "correct": False},
                    {"text": "Inflation model", "correct": False}
                ]
            },
            {
                "question": "What is the Diamond-Mortensen-Pissarides model?",
                "difficulty": "Expert",
                "descriptions": "",
                "choices": [
                    {"text": "Price theory", "correct": False},
                    {"text": "Search and matching theory in labor markets", "correct": True},
                    {"text": "International trade model", "correct": False},
                    {"text": "Financial market model", "correct": False}
                ]
            },
        ]
        
        def create_questions(category, questions_data):
            for q_data in questions_data:
                question = Question.objects.create(
                    question=q_data['question'],
                    difficulty=q_data['difficulty'],
                    category=category,
                    descriptions=q_data['descriptions']
                )
            
                for choice in q_data['choices']:
                    Choice.objects.create(
                        text=choice['text'],
                        question=question,
                        correct=choice['correct']
                    )
            

        # Populate questions for each category
        create_questions(math_category, math_data)
        create_questions(science_category, science_data)
        create_questions(finance_category, finance_data)
        create_questions(economy_category, economy_data)
        create_questions(history_category, history_data)
        self.stdout.write(
            self.style.SUCCESS('Successfully populated quiz data')
        )
