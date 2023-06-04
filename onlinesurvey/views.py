from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib import messages

from .models import Survey
from .forms import SurveyForm


def show_survey(request, id=None, access_token=None):
    survey = get_object_or_404(Survey, pk=id) # Get Survey object with the provided id. If the survey with the given id does not exist, it raises a 404 error.

    if survey.permissions == "private" and access_token != survey.access_token:
        return HttpResponseForbidden("Access Denied.")
    
    post_data = request.POST if request.method == "POST" else None
    form = SurveyForm(survey, post_data) # This line creates an instance of the SurveyForm with the survey object and the post_data as parameters. The form is used to handle user input.

    if form.is_bound and form.is_valid():
        form.save()
        messages.add_message(request, messages.INFO, 'Submissions saved.') # added message in survey.html to show the message is saved

    context = {
        "title": survey.title,
        "description": survey.description,
        "survey": survey,
        "form": form,
    }    # This dictionary contains the data to be passed to the template for rendering.
    
    return render(request, "onlinesurvey/survey.html", context)
