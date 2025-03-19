"""
	Internationalization system for Django
"""

# Authentication.models
# Define Language-Country Mapping.
COUNTRY_CHOICES = [
    ('MX', 'Mexico'),
    ('BR', 'Brazil'),
    ('US', 'United States of America'),
    ('FR', 'France'),
    ('IT', 'Italy')
]

LANGUAGE_CHOICES = [
    ('es', 'Spanish'),
    ('pt', 'Portuguese'),
    ('en', 'English'),
    ('fr', 'French'),
    ('it', 'Italian')
]

COUNTRY_TO_LANGUAGE = {
    'MX': 'es',
    'BR': 'pt',
    'US': 'en',
    'PT': 'pt',
    'FR': 'fr',
}

# Authentication.models
# Define the field on User model to add the country and language to let it to be choiceable accordingly the options we have on the lists.
country = models.CharField(max_length=2, choices=COUNTRY_CHOICES, default='US', null=False)
language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en', null=False)

# Authentication.forms
# Update the registration formulary to include a country field, based on the selected country, the language will be setter automatically.
from django import forms
from . models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model =User
        fields = ['username', 'email', 'password', 'country']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.language = COUNTRY_TO_LANGUAGE.get(self.cleaned_data['country'], 'en')
        if commit:
            user.save()
        return user
        
# Authentication.views
# Set the language in the user's session
from django.shortcuts import render, redirect
from django.utils import translation
from . forms import RegisterForm

def register(request):
    """
        Displays the registration formulary, receives the data and creates an user account.
    """
    if request.method == 'POST':
        formulary = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            tranlation.activate(user.language)
            request.session[translation.LANGUAGE_SESSION_KEY] = user.language
            return redirect('home')
        else:
            form = RegisterForm()
        return render(request, 'formularies/register.html', {'form':form})
  
# Authentication.middlewares
# Define the middleware to set language for authenticated users.
from django.utils import tranlation
from django.utils.deprecation import MiddlewareMixin

class UserLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = (request.user if request.user.is_authenticated else None)
        if user:
            user_language = user.language
            tranlation.active(user_language)
            request.LANGUAGE_CODE = tranlation.get_language()
            
# DataForge.settings
# Add the created middleware to MIDDLEWARE settings.
MIDDLEWARE = [
    ´´´
        'Authentication.middlewares.UserLanguageMiddleware',
    ´´´
]



# *apps/templates/*templates.html
# Telling HTML templates which of their content should be translated.
<h1>{% trans "Welcome to our website!" %}</h1>
<p>{% trans "Please log in to continue." %}</p>
<button>{% trans "Submit" %}</button>

# bash
# Create translation files using command lines into project directory.
django-admin makemessages -l es  # For Spanish
django-admin makemessages -l pt  # For Portuguese
django-admin makemessages -l fr  # For French

# django_project_root/local/
# The previous process will generate .po files in locale directory of the Django project.
local/es/LC_MESSAGES/django.po
local/pt/LC_MESSAGES/django.po
local/fr/LC_MESSAGES/django.po

# local/*every_language/LC_MESSAGES/django.po
# Translate every string in every .po file.
#: templates/home.html:10
msgid "Welcome to our website!"
msgstr "¡Bienvenido a nuestro sitio web!"
#: templates/home.html:12
msgid "Please log in to continue."
msgstr "Por favor, inicie sesión para continuar."
#: templates/home.html:14
msgid "Submit"
msgstr "Enviar"
# msgid: The original string (in English).
# msgstr: The translated string (in the target language).

# bash
# Compile the translation files from .po into .mo files which Django uses to serve the translations.
django-admin compilemessages


# Authentication.views
# Allow users to change their language.
from django.shortcuts import redirect
from django.utils import tranlation

def set_language(request, language_code)
    user = [request.user if request.user.is_authenticated else None]
    if user:
        user.language = language_code
        user.save()
        translation.activate(language_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = language_code
        return redirect('home')
        
# Authentication.urls
# Add an URL pattern for the view of language selection.
from django.urls import path
from . views import *

urlpatterns = [
    path('set_language/<str:language_code>/', views.set_language, name="set_language"),
]