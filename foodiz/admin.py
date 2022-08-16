from django.contrib import admin
from .models import Recipe, User, Measured_Ingredients
# ,Ingredients
# Register your models here.


admin.site.register(User)
# admin.site.register(Ingredients)
admin.site.register(Recipe)
admin.site.register(Measured_Ingredients)
    # (Ingredients)