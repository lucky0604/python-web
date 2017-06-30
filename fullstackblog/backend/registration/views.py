from django.conf import settings
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.models import Group

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework import status

from allauth.account.adapter import get_adapter
from allauth.account.views import ConfirmEmailView
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings

from backend.app_settings import (
    TokenSerializer,
    JWTSerializer,
    create_token
)

from backend.models import TokenModel
from backend.registration.serializers import (
    VerifyEmailSerializer,
)

from backend.utils import jwt_encode
from backend.views import LoginView
from .app_settings import RegisterSerializer, register_permission_classes

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2')
)


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = register_permission_classes()
    token_model = TokenModel

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(RegisterView, self).dispatch(*args, **kwargs)

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == allauth_settings.EmailVerificationMethod.MANDATORY:
            return {'detail': _('Verification email sent.')}

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'token': self.token
            }
            return JWTSerializer(data).data
        else:
            return TokenSerializer(user.auth_token).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = self.perform_create(serializer)
        user.groups.add(Group.objects.get(name = 'admin'))
        headers = self.get_success_headers(serializer.data)

        return Response(self.get_response_data(user), status = status.HTTP_201_CREATED, headers = headers)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)
        complete_signup(self.request._request, user, allauth_settings.EMAIL_VERIFICATION, None)

        return user


class VerifyEmailView(APIView, ConfirmEmailView):
    permission_classes = (AllowAny, )
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_serializer(self, *args, **kwargs):
        return VerifyEmailSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        return Response({'detail': _('ok')}, status = status.HTTP_200_OK)
