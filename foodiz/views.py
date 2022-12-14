from django.shortcuts import redirect, render
from foodiz.models import Recipe,Ingredient

from .forms import LoginForm, RecipeForm,RegisterForm,IngrediantForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def get_home (request):
    return render(request, 'home_page.html')

# def some_view(request):
#     if not request.user.is_staff:
#         raise Http404
    
# def some_view(request):
#     if request.user.is_anonymous:
#         return redirect("login")

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login (request, user)
            return redirect("recipe_list")
    context = {
        "form": form,
    }
    return render(request, 'register_page.html', context)


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect("recipe_list")
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)
    



def logout_user(request):
    logout(request)
    return redirect("home")
    
    
def get_recipe(request,recipe_id):
    try:
        recipe =Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return redirect("recipe_list")
    context = {
        "recipe": { 
            "id": recipe_id,
            "title": recipe.title, 
            "owner": recipe.owner.username,
            "describtion": recipe.describtion, 
            "serves": str(recipe.serves), 
            "time_to_prepare": str(recipe.time_to_prepare),
            "instructions": recipe.instructions,
            "ingredients_list": recipe.ingredients_list,
                #    "notes": recipe.notes,
                   "pic": recipe.pic 
                   },
}
    return render(request,"recipe_details_page.html", context)




def get_ingredient(request,ingredient_id):
    try:
        ingredient =Ingredient.objects.get(id=ingredient_id)
    except Ingredient.DoesNotExist:
        return redirect("recipe_list")
    context = {
        "ingredient": { 
            "id": ingredient_id,
            "category": ingredient.category,
            "owner": ingredient.owner.username,
           "ingredient_name":ingredient.ingredient_name,
                   },
}
    return render(request,"get_ingredient_page.html", context)



def get_recipe_list(request):
    recipes=Recipe.objects.all()
    context = {
        "recipes": recipes
    }
    return render(request,'recipe_list_page.html', context)



def get_recipe_list2(request):
    recipes=Recipe.objects.all()
    context = {
        "recipes": recipes
    }
    return render(request,'all_recipes.html', context)


def get_ingredient_list(request):
    ingredients=Ingredient.objects.all()
    context = {
        "ingredients": ingredients
    }
    return render(request,'all_ingredient.html', context)



def create_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    context = {
        "form": form,
    }
    return render(request, 'recipe_create_page.html', context)



   

def create_ingreadiant(request):
    form = IngrediantForm()
    if request.method == "POST":
        form = IngrediantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    context = {
        "form": form,
    }
    return render(request, 'ingrediant_create_page.html', context)



   



# def recipe_update(request, Recipe_id):
#     recipe = RecipeForm.objects.get(id=Recipe_id)
#     form = RecipeForm(instance=recipe)
#     if request.method == "POST":
#         form = RecipeForm(request.POST, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect("recipe_list")
#     context = {
#         "recipe": recipe,
#         "form": form,
#     }
#     return render(request, 'recipe_update_page.html', context)



    


