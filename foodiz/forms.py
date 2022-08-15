
from django import forms
from .models import Ingredients, Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'time_required', 'image', ]
        
class IngrediantForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name', 'quantity', 'unit', ]
        