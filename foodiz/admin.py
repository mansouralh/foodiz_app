from django.contrib import admin
from foodiz import models
to_register = [models.Ingredient , models.Recipe]
# Register your models here.



# admin.site.register(to_register)
# admin.site.register(User)
# # admin.site.register(Ingredients)
admin.site.register(to_register)
# admin.site.register(Measured_Ingredients)
    # (Ingredients)