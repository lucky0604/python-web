from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from backend.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView, CreateView
)

urlpatterns = [
    url(r'^password/reset/$', PasswordResetView.as_view(), name = 'rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(), name = 'rest_password_reset_confirm'),
    url(r'^login/$', LoginView.as_view(), name = 'rest_login'),
    url(r'^logout/$', LogoutView.as_view(), name = 'rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name = 'rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(), name = 'rest_password_change'),

    # articles
    url(r'articlelists/$', CreateView.as_view(), name = 'article_create')
]

urlpatterns = format_suffix_patterns(urlpatterns)
