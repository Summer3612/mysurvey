from django.contrib import admin
from django.contrib import admin
from .models import Survey, Question, Choice, Submission,Answer

'''
The admin module is a built-in application that provides a web-based interface for managing and interacting with the data stored in your Django models. 
It allows you to perform various administrative tasks such as creating, updating, and deleting model instances, managing users and permissions, and performing CRUD (Create, Read, Update, Delete) operations on your data.
Pros: Easy to use, reduce the amount of manual coding and configuration needed to handle common administration tasks.
'''

class QuestionInline(admin.TabularInline):
  # TabularInline or StackedInline allows you to display and edit related model instances inline with the parent model's admin form. 
  # By default, each inline formset displays a link that takes you to the change view of the related model instance. 
  # This link is rendered as the primary key (ID) of the related instance.
  model = Question
  show_change_link = True  # show_change_link to display a link to the change view of the related model instance.
  extra = 0

class AnswerInline(admin.TabularInline):
  model = Answer
  extra = 0

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 0

class SurveyAdmin(admin.ModelAdmin):
  # admin.ModelAdmin is a class that serves as a base class for customizing the behavior and appearance of a model in the Django admin interface. 
  # By subclassing admin.ModelAdmin and overriding its methods and attributes, you can define how the model is displayed, edited, and interacted with in the admin site.
  inlines = [
    QuestionInline
  ]
  list_display = ('title','id') # to specify the fields or methods of a model that should be displayed as columns in the list view of the admin site.

class QuestionAdmin(admin.ModelAdmin):
  inlines = [
    ChoiceInline
  ]
  
class SubmissionAdmin(admin.ModelAdmin):
    inlines = [
    AnswerInline
  ]

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Answer)