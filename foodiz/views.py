from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView
from foodiz.models import Recipe
from .forms import RecipeForm

# Create your views here.

def get_recipe(request,recipe_id):
    try:
        recipe =Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return redirect("list-page")
    context = {
        "recipe": { "id": recipe.id,
                   "title": recipe.title, 
                   "describtion": recipe.describtion, 
                   "serves": recipe.serves, 
                   "time_to_prepare": recipe.time_to_prepare,
                   "directions": recipe.directions,
                   "notes": recipe.notes,
                #    "pic": recipe.pic 
                   },
}
    return render(request, 'recipe_details_page', context)



def get_recipe_list(request):
    recipe=Recipe.objects.all()
    context = {
        "recipe": recipe,
    }
    return render(request, 'recipe_list_page.html', context)



def create_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipe-list-view")
    context = {
        "form": form,
    }
    return render(request, 'recipe_create_page.html', context)



   



def recipe_update(request, Recipe_id):
    obj = RecipeForm.objects.get(id=Recipe_id)
    form = RecipeForm(instance=obj)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("list-page")
    context = {
        "obj": obj,
        "form": form,
    }
    return render(request, 'recipe_update_page.html', context)



    


