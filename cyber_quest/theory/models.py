from django.db import models
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    about = models.CharField(max_length=255, null=False, default='text')
    themes = ArrayField(models.CharField(max_length=255), default=list, blank=True)
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    content = models.TextField(default='text')


class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, related_name='lectures', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(default='text')
