# Generated by Django 4.2.5 on 2023-12-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default='question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.TextField(default='answer'),
        ),
    ]
