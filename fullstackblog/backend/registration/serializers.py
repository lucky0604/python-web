from django.http import HttpRequest
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.utils import (email_address_exists, get_username_max_length)
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError('allauth needs to be added to INSTALLED_APPS.')

from rest_framework import serializers
from requests.exceptions import HTTPError


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length = get_username_max_length(),
        min_length = allauth_settings.USERNAME_MIN_LENGTH,
        required = allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required = allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(_('A user is already registered with this email address.'))

        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_('The two password fields did not match.'))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()