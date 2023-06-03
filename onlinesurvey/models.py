
from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)

    def __str__(self):
      return f'{self.title}'

class Question(models.Model):
    SHORT_TEXT = 'ST'
    LONG_TEXT = 'LT'
    DROPDOWN = 'DD'
    # MULTIPLE_CHOICE = 'MC'
    SINGLE_ANSWER = 'SA'
    # MULTIPLE_ANSWERS = 'MA'
    CHECKBOXES = 'CB'
    # LINEAR_SCALE = 'LS'
    DATE = 'DT'
    TIME = 'TM'
    # MULTIPLE_CHOICE_GRID = 'MCG'
    EMAIL = 'EM'
    NUMERIC = 'NM'
  
    WIDGET_TYPES = [
          (SHORT_TEXT, 'Short question (max size 255 characters)'),
          (LONG_TEXT, 'Paragraphs (max size 10,000 characters)'),
          (DROPDOWN, 'Dropdown'),
          # (MULTIPLE_CHOICE, 'Multiple Choice'),
          (SINGLE_ANSWER, 'Single correct answer'),
          # (MULTIPLE_ANSWERS, 'Multiple correct answers'),
          (CHECKBOXES, 'Checkboxes'),
          # (LINEAR_SCALE, 'Linear scale'),
          (DATE, 'Date'),
          (TIME, 'Time'),
          # (MULTIPLE_CHOICE_GRID, 'Multiple choice grid'),
          (EMAIL, 'Email'),
          (NUMERIC, 'Numeric values'),
      ]
    survey = models.ForeignKey(Survey, null=True, on_delete=models.CASCADE)
    text = models.CharField(blank=True, max_length=200)
    description = models.CharField(max_length=200, blank=True)
    widget_type = models.CharField(max_length=3, choices=WIDGET_TYPES, default='RS')
    
    def __str__(self):
      return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
      return f"{self.question.text}:{self.text}"

class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
      return f"Submission for survey:{self.survey}"

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
        return f"Answer for question {self.question} of {self.submission}"

 