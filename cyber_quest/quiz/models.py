from django.db import models
from theory.models import Course


class Test(models.Model):
    test_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='tests')

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_DIFFICULTY = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    question_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)
    text = models.TextField(blank=True)
    difficulty = models.CharField(max_length=15, choices=QUESTION_DIFFICULTY)
    age_orientation = models.CharField(max_length=50)


    def __str__(self):
        return self.text


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.question.topic} - {self.text} (Correct: {self.is_correct})'
