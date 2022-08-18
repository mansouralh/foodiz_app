from django.contrib import admin
from .models import Recipe, User, Measured_Ingredients
# ,Ingredients
# Register your models here.

from foodiz import models
to_register = [models.Measured_Ingredients, models.User, models.Recipe]

# admin.site.register(to_register)
# admin.site.register(User)
# # admin.site.register(Ingredients)
admin.site.register(Recipe)
# admin.site.register(Measured_Ingredients)
    # (Ingredients)