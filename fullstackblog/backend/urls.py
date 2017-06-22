from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

# create router and regist viewset
'''
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
'''

urlpatterns = [
#    url(r'^api/users/$', views.UserCreate.as_view(), name = 'account-create'),
    url(r'^accounts/$', views.AccountListView.as_view(), name = 'Account List'),
    url(r'^accounts/create/$', views.AccountCreateView.as_view(), name = 'Account Create'),
    url(r'^accounts/(?P<pk>[^/]+)/$', views.AccountRetrieveView.as_view(), name = 'Account Retrieve'),
    url(r'^accounts/(?P<pk>[^/]+)/update/$', views.UpdateAccountView.as_view(), name = 'Account update'),
    # url(r'^api-auth/$', views.AccountAuthenticationView.as_view(), name = 'Account Authentication'),
]