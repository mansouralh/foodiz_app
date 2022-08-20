
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
    

# ------------------------------------------------------------------------------
class Ingredient(models.Model):
    ingrediant_choices = {
        ('Vegetable','Vegetable'),('Fruits','Fruits'),('Dairy','Dairy'),('Grains','Grains'),
        ('Legumes','Legumes'),('Baked Goods','Baked Goods'),('Seafood','Seafood'),('Nuts and seeds','Nuts and seeds'),
        ('Herbs and Spices','Herbs and Spices'),('Garnishes','Garnishes'),('other','other'),('Meat','Meat'),
    }
    ingredient_name= models.CharField(max_length=250,)
    category= models.CharField(choices=ingrediant_choices , default='other',max_length=50)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.ingredient_name
    # class Meta:
    #     abstract = True
    
    
    
    
    
     
    
       


  # ------------------------------------------------------------------------------
  
class Recipe(models.Model):
    title= models.CharField(max_length=250)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    describtion= models.TextField()
    # add units to the next field >> 
    serves= models.IntegerField()
    # unit 
    time_to_prepare= models.IntegerField( )
    # preperation = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    ingredients_list = models.ManyToManyField(Ingredient, related_name="recipe")
    instructions= models.TextField()
    notes= models.TextField(null=True, blank=True)
    pic = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f"{self.title} for {self.serves} people"
    
    
# ------------------------------------------------------------------------------
 


