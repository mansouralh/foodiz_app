# Generated by Django 4.1 on 2022-08-16 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodiz', '0004_alter_measured_ingredients_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measured_ingredients',
            name='category',
            field=models.CharField(choices=[('Garnishes', 'Garnishes'), ('Seafood', 'Seafood'), ('Vegetable', 'Vegetable'), ('Grains', 'Grains'), ('Baked Goods', 'Baked Goods'), ('Dairy', 'Dairy'), ('Fruits', 'Fruits'), ('Legumes', 'Legumes'), ('Nuts and seeds', 'Nuts and seeds'), ('other', 'other'), ('Herbs and Spices', 'Herbs and Spices')], default='other', max_length=50),
        ),
    ]