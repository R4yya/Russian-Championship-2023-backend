from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'title', 'about', 'themes', 'image', 'price')
    search_fields = ('title', 'category')
    list_display_links = ('title',)
