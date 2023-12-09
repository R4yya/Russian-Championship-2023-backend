from rest_framework import serializers
from .models import Question, Answer, Test


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'topic', 'course', 'test', 'text', 'difficulty', 'age_orientation']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer_id', 'question', 'text', 'is_correct']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['test_id', 'title', 'course']
