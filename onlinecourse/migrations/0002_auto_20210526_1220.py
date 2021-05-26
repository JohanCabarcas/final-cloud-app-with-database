# Generated by Django 3.1.3 on 2021-05-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='choices',
        ),
        migrations.AddField(
            model_name='submission',
            name='choice',
            field=models.ManyToManyField(to='onlinecourse.Choice'),
        ),
    ]
