from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView
from foodiz.models import Recipe
from .forms import RecipeForm

# Create your views here.

def get_recipe(request,recipe_id):
    try:
        recipe =Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return redirect("recipe_list")
    context = {
        "recipe": { 
            "id": recipe_id,
            "title": recipe.title, 
            "describtion": recipe.describtion, 
            "serves": str(recipe.serves), 
            "time_to_prepare": str(recipe.time_to_prepare),
            "directions": recipe.directions,
                #    "notes": recipe.notes,
                #    "pic": recipe.pic 
                   },
}
    return render(request,"recipe_details_page.html", context)



def get_recipe_list(request):
    recipes=Recipe.objects.all()
    context = {
        "recipes": recipes
    }
    return render(request,'recipe_list_page.html', context)



def create_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    context = {
        "form": form,
    }
    return render(request, 'recipe_create_page.html', context)



   



def recipe_update(request, Recipe_id):
    recipe = RecipeForm.objects.get(id=Recipe_id)
    form = RecipeForm(instance=recipe)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    context = {
        "recipe": recipe,
        "form": form,
    }
    return render(request, 'recipe_update_page.html', context)



    


