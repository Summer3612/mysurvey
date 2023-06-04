
from django.db import models
import uuid

class Survey(models.Model):
    PERMISSION_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    # blank = False to make the title mandatory and True means it is optional
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    permissions = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default='public')
    access_token = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if self.permissions == 'private' and not self.access_token:
            self.access_token = uuid.uuid4()

        super().save(*args, **kwargs)
        return self.access_token
    
    def __str__(self):
        return f'{self.title}'

class Question(models.Model):
    SHORT_TEXT = 'ST'
    LONG_TEXT = 'LT'
    DROPDOWN = 'DD'
    SINGLE_ANSWER = 'SA'
    CHECKBOXES = 'CB'
    DATE = 'DT'
    TIME = 'TM'
    EMAIL = 'EM'
    NUMERIC = 'NM'
  
    WIDGET_TYPES = [
          (SHORT_TEXT, 'Short question (max size 255 characters)'),
          (LONG_TEXT, 'Paragraphs (max size 10,000 characters)'),
          (DROPDOWN, 'Dropdown'),
          (SINGLE_ANSWER, 'Single correct answer'),
          (CHECKBOXES, 'Checkboxes'),
          (DATE, 'Date'),
          (TIME, 'Time'),
          (EMAIL, 'Email'),
          (NUMERIC, 'Numeric values'),
      ]
    survey = models.ForeignKey(Survey, null=True, on_delete=models.CASCADE)
    text = models.CharField(blank=False, max_length=255)
    description = models.CharField(max_length=255, blank=True)
    widget_type = models.CharField(max_length=3, choices=WIDGET_TYPES)
    
    def __str__(self):
      return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=255,blank=True)

    def __str__(self):
      return f"{self.question.text}:{self.text}"

class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
      return f"Submission {self.id} for {self.survey}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='answers')

    text_answer = models.CharField(max_length=10000, blank=True, null=True)  
    short_answer = models.CharField(max_length=255, blank=True, null=True)
    choice_answer = models.ForeignKey(Choice, on_delete=models.SET_NULL, blank=True, null=True)
    date_answer = models.DateField(blank=True, null=True)
    time_answer = models.TimeField(blank=True, null=True)
    email_answer = models.EmailField(blank=True, null=True)
    integer_answer = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"Answer for {self.question} of {self.submission}"

 