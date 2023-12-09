from django.contrib import admin
from .models import Course, Article, Lecture


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'title', 'about', 'themes', 'image', 'price')
    search_fields = ('title', 'category')
    list_display_links = ('title',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'title', 'image', 'content')
    search_fields = ('title', 'content')
    list_display_links = ('title',)


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('lecture_id', 'course', 'title', 'content', 'order')
    search_fields = ('title', 'content')
    list_display_links = ('title',)
