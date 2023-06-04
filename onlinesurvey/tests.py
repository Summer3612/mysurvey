from django.test import TestCase
from django.urls import reverse

from .models import Survey,Question

class SurveyTestCase(TestCase):
    def setUp(self):
        self.survey = Survey.objects.create(
            title='Test Survey',
            description='This is a test survey',
            permissions = 'public'
        )
        self.question1 = Question.objects.create(
            survey=self.survey,
            text='Question 1',
            widget_type='ST'
        )

    def test_survey_creation(self):
        self.assertEqual(self.survey.title, 'Test Survey')
        self.assertEqual(self.survey.description, 'This is a test survey')
        self.assertEqual(self.survey.permissions, 'public')
    
    def test_question_creation(self):
        self.assertEqual(self.question1.text, 'Question 1')
        self.assertEqual(self.question1.widget_type, 'ST')

    def test_survey_detail_view(self):
        response = self.client.get(reverse('show-public-survey', args=[self.survey.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Survey')
        self.assertContains(response, 'This is a test survey')

