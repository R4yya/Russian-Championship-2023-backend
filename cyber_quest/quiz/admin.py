from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'topic', 'text', 'difficulty', 'age_orientation')
    search_fields = ('topic', 'difficulty')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'question', 'text', 'is_correct')
    search_fields = ('question', 'is_correct')

