# Generated by Django 3.2.19 on 2023-06-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0003_alter_movie_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
