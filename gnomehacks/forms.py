from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, DateTimeInput, Form, ModelForm, PasswordInput

from .models import Hackfest, Location


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ["name", "city", "country", "address", "description"]


class HackfestForm(ModelForm):
    class Meta:
        model = Hackfest
        fields = ["title", "location", "start", "end", "description"]
        widgets = {
            "start": DateTimeInput(attrs={"type": "datetime-local"}),
            "end": DateTimeInput(attrs={"type": "datetime-local"}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(Form):
    username = CharField(max_length=200)
    password = CharField(max_length=200, widget=PasswordInput)
