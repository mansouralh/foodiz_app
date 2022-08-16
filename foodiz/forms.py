
from django import forms
from .models import Ingredients, Recipe
# ,
# Measured_Ingredients

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'describtion', 'serves', 'time_to_prepare', 'directions', 'notes', 'pic']
        
# class IngrediantForm(forms.ModelForm):
#     class Meta:
#         model = Measured_Ingredients
#         fields = [ 'quantity', 'unit', ]
        