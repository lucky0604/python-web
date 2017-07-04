"""fullstackblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^rest-auth/', include('backend.urls')),
    url(r'^rest-auth/registration/', include('backend.registration.urls')),
   
    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name = 'profile-redirect'),
    url(r'^docs/$', get_swagger_view(title='API docs'), name = 'api_docs'),
    url(r'^$', TemplateView.as_view(template_name = 'index.html')),
    url(r'^api/post/', include('backend.posts.urls', namespace="posts-api")),
]
