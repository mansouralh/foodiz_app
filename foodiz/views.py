from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView
from foodiz.models import Recipe
from .forms import RecipeForm

# Create your views here.



class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    
    
    
# class RecipeCreateView(CreateAPIView):
#     serializer_class = CreateSerializer


def home(request):
    context = {
        "title": "Home",
        "header": "Welcome to our site!",
    }
    return render(request, "home_page.html", context)
    
    
    
def detail_view(request):
    context = {
        "object": {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
            "key4": "value4",
        },
    }
    return render(request, 'detail_page.html', context)


def article_detail(request):
    context = {
        "article": {
            "title": "Do or do not",
            "content": "There is no try.",
            "author": "Yoda",
            "created_on": "2018-2-12",
            "last_updated_on": "2018-2-14",
        },
    }
    return render(request, "article_detail_page.html", context)




def list_view(request):
    context = {
        "object_list": [
            {
                "key1": "value1",
                "key2": "value2",
            },
            {
                "key1": "value1",
                "key2": "value2",
            },
            {
                "key1": "value1",
                "key2": "value2",
            },
        ],
    }
    return render(request, "list_page.html", context)


def article_list(request):
    context = {
        "articles": [
            {
                "title": "Do or do not",
                "author": "Yoda",
            },
            {
                "title": "Youre my only hope",
                "author": "Leia Organa",
            },
            {
                "title": "I find your lack of faith disturbing.",
                "author": "Darth Vader",
            },
        ],
    }
    return render(request, "article_list_page.html", context)









def recipe_create_view(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list-view")
    context = {
        "form": form,
    }
    return render(request, 'recipe_create_page.html', context)



def recipe_update_view(request, obj_id):
    obj = RecipeForm.objects.get(id=obj_id)
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



def recipe_delete_view(request, object_id):
    Recipe.objects.get(id=object_id).delete()
    return redirect("list-view")
    
# def get_recipe(request):
#     return render(request, 'recipe.html')

# def get_ingredients(request):
#     return render(request, 'ingredients.html')

# def get_home(request):
#     return render(request, 'home.html')

# def get_user(request):
#     return render(request, 'user.html')

