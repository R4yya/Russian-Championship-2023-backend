from django.db import models


class Theory(models.Model):
    ARTICLE_CATEGORIES = [
        ('news', 'News'),
        ('lecture', 'Lecture'),
        ('theory', 'Theory'),
        ('article', 'Article'),
        ('course', 'Course'),
    ]

    theory_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False, default='text')
    sub_title = models.CharField(max_length=255, null=False, default='text')
    content = models.TextField(default='text')
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    category = models.CharField(max_length=10, choices=ARTICLE_CATEGORIES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
