# Generated by Django 3.0.8 on 2021-01-04 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0025_main_food_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_food',
            name='picture',
        ),
    ]
