# Generated by Django 4.2.7 on 2023-12-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-06-03'),
            preserve_default=False,
        ),
    ]
