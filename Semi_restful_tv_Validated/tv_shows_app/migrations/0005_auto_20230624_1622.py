# Generated by Django 3.2.19 on 2023-06-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0004_auto_20230624_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]