# Generated by Django 3.0.3 on 2020-03-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_expenses', '0002_auto_20200227_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(max_length=255, null=True),
        ),
    ]
