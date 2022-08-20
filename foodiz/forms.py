
from tkinter import Widget
from django import forms
from .models import Recipe,Ingredient
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',] 
        Widget = {forms.PasswordInput(),}
        

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'owner','describtion', 'serves', 'time_to_prepare','ingredients_list', 'instructions', 'notes', 'pic']
        
class IngrediantForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [ 'ingredient_name','category', 'owner', ]
        