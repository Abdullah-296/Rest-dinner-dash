# Generated by Django 4.0.6 on 2022-08-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindisplay', '0005_itemimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(help_text='link your item to category', to='maindisplay.category'),
        ),
    ]
