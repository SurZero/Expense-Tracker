# Generated by Django 3.0.3 on 2020-03-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_expenses', '0003_auto_20200303_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
