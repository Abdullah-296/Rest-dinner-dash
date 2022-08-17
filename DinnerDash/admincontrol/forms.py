
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

def emailvalidation(value):
    all_user = User.objects.all()
    for user in all_user:
        if user.email == value:
            raise forms.ValidationError("Email Already exist")


def usernamevalidation(value):
    if len(value) < 2:
        raise forms.ValidationError("Username can be less than 2 characters")
    else:
        all_user = User.objects.all()
        for user in all_user:
            if user.username == value:
                raise forms.ValidationError("Username Already exist")


def special_character_validation(value):
    match = re.fullmatch('[A-Za-z0-9_.]{2,32}( [A-Za-z]{2,32})?', value)
    if match is None:
        raise forms.ValidationError("This field only accept character , Numbers, _ and . ")


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=32, required=True, min_length=2, help_text='username',
                               validators=[usernamevalidation, special_character_validation], widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Username'}))

    first_name = forms.CharField(max_length=32, required=True, min_length=2, help_text='Enter First name.',
                                 validators=[special_character_validation],
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    last_name = forms.CharField(max_length=32, required=True, min_length=2, help_text='Enter Last name.',
                                validators=[special_character_validation],
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                             validators=[emailvalidation], widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': 'abd@xyz.com'}))

    password1 = forms.CharField(max_length=32, min_length=8, widget=forms.PasswordInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': '*****',
                    }))

    password2 = forms.CharField(max_length=32, min_length=8, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '*****',
        }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(max_length=32,
                             required=True,
                             min_length=2,
                             validators=[special_character_validation],
                             widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': 'Username'}))

    password = forms.CharField(max_length=32, min_length=5, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '*****',
        }
    ))
