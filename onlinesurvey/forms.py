from django import forms
from .models import Submission, Choice

class PlainTextWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return value

class SurveyForm(forms.Form):
  
    # question_1 = forms.ChoiceField(widget=forms.RadioSelect, choices=())

    def __init__(self, survey, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.survey = survey
        # del self.fields["question_1"]
        # self.fields["Survey"] = forms.CharField(initial=survey.title, disabled=True,widget=PlainTextWidget())
        # self.fields["description"] = forms.CharField(initial=survey.description, disabled=True,widget=PlainTextWidget())
  
        for question in survey.question_set.all():
              choices = [(choice.id, choice.text) for choice in question.choice_set.all()]
              field_mapping = {
              'ST': forms.CharField(max_length=255),
              'LT': forms.CharField(widget=forms.Textarea),
              'DD': forms.ChoiceField(widget=forms.Select, choices=choices),
            #   'MC': forms.MultipleChoiceField(choices=choices),
              'SA': forms.ChoiceField(widget=forms.RadioSelect, choices=choices),
            #   'MA': forms.MultipleChoiceField(choices=choices),  
              'CB': forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices),
            #   'LS': forms.IntegerField(),  
              'DT': forms.DateField(),
              'TM': forms.TimeField(),
            #   'MCG': forms.MultipleChoiceField(choices=choices),  
              'EM': forms.EmailField(),
              'NM': forms.IntegerField(),  # Or forms.DecimalField if you need to support decimal numbers
          }

            # Get the correct form field for this question type
              field_class = field_mapping.get(question.widget_type)

              # Create the form field
              self.fields[f"question_{question.id}"] = field_class
              self.fields[f"question_{question.id}"].label = question.text
        
    def save(self):
        data = self.cleaned_data
        submission = Submission(survey=self.survey)
        submission.save()

        for question in self.survey.question_set.all():
            answer_data = data.get(f"question_{question.id}")
            if answer_data:
                if question.widget_type in ['DD', 'MC', 'SA', 'MA', 'CB', 'MCG']:
                    if isinstance(answer_data, list):  # Handle multiple answers.
                        choices = Choice.objects.filter(id__in=answer_data)
                        for choice in choices:
                            submission.answers.create(choice_answer=choice, question=question)
                    else:  # Handle single answer.
                        choice = Choice.objects.get(pk=answer_data)
                        submission.answers.create(choice_answer=choice, question=question)
                elif question.widget_type in ['ST', 'LT']:
                    submission.answers.create(text_answer=answer_data, question=question)
                elif question.widget_type == 'LS':
                    submission.answers.create(integer_answer=int(answer_data), question=question)
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