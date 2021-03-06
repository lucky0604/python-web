from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password_type = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password_type(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_type']:
            raise forms.ValidationError('Password do not match!')
        return cd['password_type']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
