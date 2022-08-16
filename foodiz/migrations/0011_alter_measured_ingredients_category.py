# Generated by Django 4.1 on 2022-08-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodiz', '0010_alter_measured_ingredients_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measured_ingredients',
            name='category',
            field=models.CharField(choices=[('other', 'other'), ('Dairy', 'Dairy'), ('Seafood', 'Seafood'), ('Vegetable', 'Vegetable'), ('Garnishes', 'Garnishes'), ('Nuts and seeds', 'Nuts and seeds'), ('Fruits', 'Fruits'), ('Grains', 'Grains'), ('Baked Goods', 'Baked Goods'), ('Herbs and Spices', 'Herbs and Spices'), ('Legumes', 'Legumes')], default='other', max_length=50),
        ),
    ]
