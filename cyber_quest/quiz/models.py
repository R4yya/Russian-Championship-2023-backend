from django.db import models


class Question(models.Model):
    QUESTION_DIFFICULTY = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    question_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    text = models.TextField(default='question')
    difficulty = models.CharField(max_length=15, choices=QUESTION_DIFFICULTY)
    age_orientation = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.topic} - {self.difficulty}"


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField(default='answer')
    is_correct = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.question.topic} - {self.text} (Correct: {self.is_correct})"
