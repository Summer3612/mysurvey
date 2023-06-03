from django.test import TestCase
from django.urls import reverse

from .models import Survey

class SurveyTestCase(TestCase):
    def setUp(self):
        self.survey = Survey.objects.create(
            title='Test Survey',
            description='This is a test survey'
        )

    def test_survey_creation(self):
        self.assertEqual(self.survey.title, 'Test Survey')
        self.assertEqual(self.survey.description, 'This is a test survey')

    def test_survey_detail_view(self):
        response = self.client.get(reverse('survey-detail', args=[self.survey.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Survey')
        self.assertContains(response, 'This is a test survey')

    def test_survey_creation_view(self):
        data = {
            'title': 'New Survey',
            'description': 'This is a new survey'
        }
        response = self.client.post(reverse('survey-create'), data=data)
        self.assertEqual(response.status_code, 302)

        new_survey = Survey.objects.last()
        self.assertEqual(new_survey.title, 'New Survey')
        self.assertEqual(new_survey.description, 'This is a new survey')

    def test_survey_update_view(self):
        data = {
            'title': 'Updated Survey',
            'description': 'This is an updated survey'
        }
        response = self.client.post(reverse('survey-update', args=[self.survey.id]), data=data)
        self.assertEqual(response.status_code, 302)

        updated_survey = Survey.objects.get(id=self.survey.id)
        self.assertEqual(updated_survey.title, 'Updated Survey')
        self.assertEqual(updated_survey.description, 'This is an updated survey')

    def test_survey_delete_view(self):
        response = self.client.post(reverse('survey-delete', args=[self.survey.id]))
        self.assertEqual(response.status_code, 302)

        with self.assertRaises(Survey.DoesNotExist):
            Survey.objects.get(id=self.survey.id)

    # Add more test cases for other functionality as needed

