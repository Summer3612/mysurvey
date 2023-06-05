'''
When you define models in Django, they are translated into database tables. 
Migrations help you keep track of any changes you make to your models and provide a way to apply those changes to the database. 
Migrations are essentially Python files that describe the changes you want to make to the database schema.
'''

from django.db import models
import uuid

'''
The models module facilitates the creation and manipulation of database models by providing a set of classes and functions that. 
The models module is a core component of Django's Object-Relational Mapping (ORM) system.
Advantage: It abstracts the database interactions and allows you to work with databases using Python code.

'''
class Survey(models.Model):
    PERMISSION_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    # requirements: blank = False to make the title mandatory and True means it is optional
    title = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True)
    permissions = models.CharField(max_length=10, choices=PERMISSION_CHOICES, default='public')
    access_token = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if self.permissions == 'private' and not self.access_token:
            self.access_token = uuid.uuid4()
        super().save(*args, **kwargs)   # It calls the save() method of the parent class to perform the actual saving of the object to the database.
        return self.access_token
    
    # The __str__() method in Django models is used to define a human-readable string representation of an object. 
    # It is a built-in Python method that gets called when you try to convert an object to a string
    # especially important when you print the object or display it in the Django admin interface.
    def __str__(self):
        return f'{self.title}'

class Question(models.Model):
    # capitalised as the value should be constant
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
    
    # 5.	Each question has following 3 sections:
    text = models.CharField(blank=False, max_length=255)
    description = models.CharField(max_length=255, blank=True)
    widget_type = models.CharField(max_length=3, choices=WIDGET_TYPES)
    
    def __str__(self):
      return f" Question: {self.text} -> {self.survey}"

class Choice(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=255,blank=True)

    def __str__(self):
      return f"{self.question.text}:{self.text}"

class Submission(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
      return f"Submission {self.id} -> {self.survey}"

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
        return f"Answer for {self.question} | {self.submission}"
