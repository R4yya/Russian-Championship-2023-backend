from django.contrib import admin
from .models import Question, Answer, Test


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'topic', 'course', 'test', 'text', 'difficulty', 'age_orientation')
    search_fields = ('topic', 'difficulty')
    list_display_links = ('topic',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'question', 'text', 'is_correct')
    search_fields = ('question', 'is_correct')
    list_display_links = ('question',)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('test_id', 'title', 'course',)
    search_fields = ('title', 'course')
    list_display_links = ('title',)

