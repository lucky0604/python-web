from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter

# create router and regist viewset
router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
#    url(r'^api/users/$', views.UserCreate.as_view(), name = 'account-create'),
    url(r'^', include(router.urls)),
]
