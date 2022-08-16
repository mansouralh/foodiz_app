# Generated by Django 4.1 on 2022-08-15 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measured_Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients_name', models.CharField(max_length=250)),
                ('category', models.CharField(choices=[('Herbs and Spices', 'Herbs and Spices'), ('other', 'other'), ('Garnishes', 'Garnishes'), ('Dairy', 'Dairy'), ('Legumes', 'Legumes'), ('Seafood', 'Seafood'), ('Baked Goods', 'Baked Goods'), ('Grains', 'Grains'), ('Vegetable', 'Vegetable'), ('Fruits', 'Fruits'), ('Nuts and seeds', 'Nuts and seeds')], default='other', max_length=50)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('describtion', models.TextField()),
                ('serves', models.IntegerField()),
                ('time_to_prepare', models.IntegerField()),
                ('directions', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodiz.user')),
                ('preperation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodiz.measured_ingredients')),
            ],
        ),
        migrations.AddField(
            model_name='measured_ingredients',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodiz.user'),
        ),
    ]
