from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Survey, Question, Choice, Submission,Answer

class QuestionInline(admin.TabularInline):
  model = Question
  show_change_link = True
  extra = 0

class AnswerInline(admin.TabularInline):
  model = Answer
  show_change_link = True
  extra = 0

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 0

class SurveyAdmin(admin.ModelAdmin):
  inlines = [
    QuestionInline
  ]
  list_display = ('title','id')

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
admin.site.register(Submission,SubmissionAdmin)
admin.site.register(Answer)