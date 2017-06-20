from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import detail_route, list_route
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import authentication, permissions

# add token support
from rest_framework.authtoken.models import Token

'''
class UserCreate(APIView):
    # create the user
    def post(self, request, format = 'json'):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                # create a token after a successful registration
                token = Token.objects.create(user = user)
                json = serializer.data
                json['token'] = token.key
                # token response must use Response(json)
                return Response(json, status = status.HTTP_201_CREATED)
#                return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
'''

# use viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods = ['post'])
    def post(self, request, format = 'json'):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
