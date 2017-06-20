'''
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
'''


from rest_framework import (
    generics, permissions, views, response, status
)
from .models import Account
from .serializers import (
    AccountCreateSerializer,
    AccountSerializer,
    AuthenticateSerializer,
    UpdateAccountSerializer,
    AccountRetrieveSerializer
)

class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
    permission_classes = [permissions.AllowAny]

class AccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccountRetrieveView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRetrieveSerializer

class UpdateAccountView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = UpdateAccountSerializer

class AccountAuthenticationView(views.APIView):
    queryset = Account.objects.all()
    serializer_class = AuthenticateSerializer

    def post(self, request):
        data = request.data
        serializer = AuthenticateSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            new_date = serializer.data
            return response.Response(new_date, status = status.HTTP_200_OK)
        return response.Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
