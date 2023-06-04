from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib import messages

from .models import Survey
from .forms import SurveyForm


def show_survey(request, id=None, access_token=None):
    
    # Get Survey object with the provided id. 
    # If the survey with the given id does not exist, it raises a 404 error.
    survey = get_object_or_404(Survey, pk=id)

    if survey.permissions == "private" and access_token != survey.access_token:
        return HttpResponseForbidden("Access Denied.")
    
    post_data = request.POST if request.method == "POST" else None
    # This line creates an instance of the SurveyForm with the survey object and the post_data as parameters. The form is used to handle user input.
    form = SurveyForm(survey, post_data)

    if form.is_bound and form.is_valid():
        form.save()
        # added message in survey.html to show on the page that the message is saved
        messages.add_message(request, messages.INFO, 'Submissions saved.')
    
    # This dictionary contains the data to be passed to the template for rendering.
    context = {
        "title": survey.title,
        "description": survey.description,
        "survey": survey,
        "form": form,
    }
    return render(request, "onlinesurvey/survey.html", context)
