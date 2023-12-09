from django.contrib import admin
from .models import AppUser, Achievement


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'age', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('achievement_id', 'name', 'description', 'is_gained')
    search_fields = ('name', 'description')
