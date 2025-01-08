# Quiz Web Application

A web-based quiz application built with Django and MySQL.

## Description
This application allows users to take quizzes through a web interface. It features an admin panel for quiz management and a user-friendly interface for quiz-takers.

## Prerequisites
- Python 3.x
- MySQL
- pip (Python package manager)

## Installation

### 1. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv myenv

# Activate virtual environment
source myenv/bin/activate   # On Linux/Mac
# or
myenv\Scripts\activate      # On Windows
```

### 2. Database Setup
```sql
CREATE DATABASE dbquizz;
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database Connection
Navigate to `backend/backend/settings.py` and update the `DATABASES` configuration with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbquizz',
        'USER': 'root',
        'PASSWORD': 'your_password_here',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Initialize the Quiz Data
```bash
python manage.py populate_quiz
```

### 6. Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application:
   - Quiz Interface: [http://localhost:8000/quizz/](http://localhost:8000/quizz/)
   - Admin Panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Project Structure
```
backend/
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   └── ...
└── ...
```

## Additional Notes
- Make sure MySQL server is running before starting the application
- Keep your virtual environment activated while working on the project
- Ensure all required ports are available (especially 8000 for Django and 3306 for MySQL)
