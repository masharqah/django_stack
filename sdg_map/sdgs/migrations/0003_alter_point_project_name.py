# Generated by Django 3.2.19 on 2023-08-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdgs', '0002_auto_20230808_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='Project_name',
            field=models.CharField(max_length=250),
        ),
    ]
