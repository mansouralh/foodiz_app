"""webproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from foodiz.views import get_recipe,create_recipe,get_recipe_list ,get_home,register_user,login_user,get_ingredient,get_recipe_list2,get_ingredient_list,create_ingreadiant,logout_user


urlpatterns = [
    path ("", get_home, name="home"),
    path('admin/', admin.site.urls),
    path("recipes/", get_recipe_list,name="recipe_list"),
    path("recipes2/", get_recipe_list2,name="recipe_lists2"),
    path("create_recipe/", create_recipe,name="recipe_form"),
    path("create_ingreadiant/", create_ingreadiant,name="create_ingreadiant"),
    path("recipe_details/<int:recipe_id>/", get_recipe,name="recipe_detail"),
    path("register/", register_user,name="register"),
    path("login_user/", login_user,name="login_user"),
    path("get_ingredient/", get_ingredient,name="get_ingredient"),
    path("ingredient_list/", get_ingredient_list,name="ingredient_list"),
    path("logout_user/", logout_user,name="logout_user"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    