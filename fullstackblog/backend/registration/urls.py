from django.views.generic import TemplateView
from django.conf.urls import url

from .views import RegisterView, VerifyEmailView

urlpatterns = [
    url(r'^$', RegisterView.as_view(), name = 'rest_register'),
    url(r'^verify-email/$', VerifyEmailView.as_view(), name = 'rest_verify_email'),
]
