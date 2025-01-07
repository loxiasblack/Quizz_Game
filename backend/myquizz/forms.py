from django import forms
from .models import CustomUser, Question

SEXE_CHOICES = {
    'male':'Male', 
    'female': 'Female'}

class RegisterForms(forms.ModelForm):
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter a secure password',
        }),
        label="Password"
    )
    sexe = forms.ChoiceField(
        choices=SEXE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Gender"
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'birth_date', 'sexe']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'birth_date': 'Date of Birth',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your email'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date',
                'placeholder': 'YYYY-MM-DD'
            }),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        label='Password'
    )

class ProfilePictureForm(forms.Form):
    profile_picture=forms.ImageField(label='Upload Profile Picture')
    

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        
    def clean_points(self):
        points = self.cleaned_data.get('points')
        if points < 0:
            raise forms.ValidationError("Points must be non-negative.")
        return points

class categoryAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
