from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User

# add token support
from rest_framework.authtoken.models import Token

# Create your views here.
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
