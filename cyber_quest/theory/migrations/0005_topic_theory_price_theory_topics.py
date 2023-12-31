# Generated by Django 4.2.5 on 2023-12-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theory', '0004_rename_sub_title_theory_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='theory',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='theory',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='theories', to='theory.topic'),
        ),
    ]
