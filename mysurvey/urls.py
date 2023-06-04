"""
URL configuration for mysurvey project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

'''
When a user makes a request to a specific URL, Django's URL resolver takes the requested URL and tries to match it against the defined URL patterns in the urlpatterns. Once a match is found, Django calls the associated view function, passing the request and any captured URL parameters as arguments.
'''
from django.contrib import admin
from django.urls import path
from onlinesurvey.views import show_survey

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey/<int:id>/', show_survey, name='show-public-survey'),
    path("survey/<int:id>/<access_token>/", show_survey, name="show-private-survey"),
]
