# Generated by Django 3.0.8 on 2020-12-26 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0009_main_food_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_user',
            name='favourite_foods',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_fav_food', to='health.Main_food'),
        ),
        migrations.AlterField(
            model_name='main_food',
            name='creator',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_food', to=settings.AUTH_USER_MODEL),
        ),
    ]
