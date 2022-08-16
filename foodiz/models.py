
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    

# ------------------------------------------------------------------------------
class Ingredients(models.Model):
    ingrediant_choices = {
        ('Vegetable','Vegetable'),('Fruits','Fruits'),('Dairy','Dairy'),('Grains','Grains'),
        ('Legumes','Legumes'),('Baked Goods','Baked Goods'),('Seafood','Seafood'),('Nuts and seeds','Nuts and seeds'),
        ('Herbs and Spices','Herbs and Spices'),('Garnishes','Garnishes'),('other','other'),
    }
    ingredients_name= models.CharField(max_length=250,)
    category= models.CharField(choices=ingrediant_choices , default='other',max_length=50)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.name
    class Meta:
        abstract = True
    
    
    
    
    
     # ------------------------------------------------------------------------------
    
       
class Measured_Ingredients(Ingredients):
    # ingredients= models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    # recipe= models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity= models.IntegerField()
    unit= models.CharField(max_length=10)
    def __str__(self):
        return self.ingredients_name

  # ------------------------------------------------------------------------------
  
class Recipe(models.Model):
    title= models.CharField(max_length=250)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    describtion= models.TextField()
    # add units to the next field >> 
    serves= models.IntegerField()
    # unit 
    time_to_prepare= models.IntegerField( )
    preperation = models.ForeignKey(Measured_Ingredients, on_delete=models.CASCADE)
    # preperation = models.ManyToManyField(Ingredients,through="Measured_Ingredients", related_name="preperation")
    directions= models.TextField()
    notes= models.TextField(null=True, blank=True)
    pic = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title
    
    
# ------------------------------------------------------------------------------
 


