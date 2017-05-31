from rest_framework import generics
from ..models import Subject, Course
from .serializers import SubjectSerializer, CourseSerializer

# building custom views
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

# authentication
from rest_framework.authentication import BasicAuthentication

# permissions
from rest_framework.permissions import IsAuthenticated

# creating view sets and routers
from rest_framework import viewsets

# adding additional actions to view sets
from rest_framework.decorators import detail_route

from .permissions import IsEnrolled
from .serializers import CourseWithContentsSerializer

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

'''
class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated,)
    def post(self, request, pk, format = None):
        course = get_object_or_404(Course, pk = pk)
        course.students.add(request.user)
        return Response({'enrolled': True})
'''

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # change the view into a custom view set action
    @detail_route(methods = ['post'], authentication_classes = [BasicAuthentication], permission_classes = [IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    # create a view that mimics the behavior of the 'retrieve()' action but includes the course contents
    @detail_route(methods = ['get'], serializer_class = CourseWithContentsSerializer, authentication_classes = [BasicAuthentication], permission_classes = [IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
