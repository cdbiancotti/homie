# Generated by Django 4.1.1 on 2023-08-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
