# Generated by Django 5.0 on 2024-02-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
