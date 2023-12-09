from django.contrib import admin
from .models import Theory


@admin.register(Theory)
class TheoryAdmin(admin.ModelAdmin):
    list_display = ('theory_id', 'title', 'sub_title', 'content', 'image', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'category')
