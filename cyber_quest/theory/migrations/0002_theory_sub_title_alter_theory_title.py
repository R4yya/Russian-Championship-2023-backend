# Generated by Django 4.2.5 on 2023-12-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theory',
            name='sub_title',
            field=models.CharField(default='text', max_length=255),
        ),
        migrations.AlterField(
            model_name='theory',
            name='title',
            field=models.CharField(default='text', max_length=255),
        ),
    ]