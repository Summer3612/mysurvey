from django import forms
from .models import Submission, Choice

'''
The forms module provides a way to define and handle HTML forms in a web application,i.e. used to automatically generate HTML for elements from classes.
In Django, the most common form submission is a post request, which will send the data down in the post body.
The server-side code captures user input, validates it, and processes it on the server side. 
The forms module in Django offers a set of powerful features to simplify form handling and data validation.
'''

class SurveyForm(forms.Form):
    def __init__(self, survey, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.survey = survey

        for question in survey.question_set.all():
              choices = [(choice.id, choice.text) for choice in question.choice_set.all()]
              field_mapping = {
              'ST': forms.CharField(max_length=255),
              'LT': forms.CharField(widget=forms.Textarea),
              'DD': forms.ChoiceField(widget=forms.Select, choices=choices),
              'SA': forms.ChoiceField(widget=forms.RadioSelect, choices=choices),
              'CB': forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices),
              'DT': forms.DateField(),
              'TM': forms.TimeField(),
              'EM': forms.EmailField(),
              'NM': forms.IntegerField(),  # Or forms.DecimalField if you need to support decimal numbers
          }
              field_class = field_mapping.get(question.widget_type)# Get the correct form field for this question type
              # Create the form field
              self.fields[f"question_{question.id}"] = field_class
              self.fields[f"question_{question.id}"].label = question.text
        
    def save(self):
        data = self.cleaned_data  # This step is essential to prevent potential issues like code injection or unexpected behavior when saving the form data to the database.
        submission = Submission(survey=self.survey)
        submission.save()

        for question in self.survey.question_set.all():
            answer_data = data.get(f"question_{question.id}")
            if answer_data:
                if question.widget_type == 'CB':
                    choices = Choice.objects.filter(id__in=answer_data)
                    for choice in choices:
                        submission.answers.create(choice_answer=choice, question=question)
                elif question.widget_type in ['DD','SA']:
                        choice = Choice.objects.get(pk=answer_data)
                        submission.answers.create(choice_answer=choice, question=question)
                elif question.widget_type == 'ST':
                    submission.answers.create(short_answer=answer_data, question=question)
                elif question.widget_type == 'LT':
                    submission.answers.create(text_answer=answer_data, question=question)
                elif question.widget_type == 'DT':
                    submission.answers.create(date_answer=answer_data, question=question)
                elif question.widget_type == 'TM':
                    submission.answers.create(time_answer=answer_data, question=question)
                elif question.widget_type == 'EM':
                    submission.answers.create(email_answer=answer_data, question=question)
                elif question.widget_type == 'NM':
                    submission.answers.create(integer_answer=int(answer_data), question=question)

        submission.save()
        return submission
