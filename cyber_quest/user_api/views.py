from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserRegister(APIView):
    permission_classes = (AllowAny,)


    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                token = RefreshToken.for_user(user)
                data = serializer.data
                data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
                return Response(data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    permission_classes = (AllowAny,)


    def post(self, request):

        data = request.data

        assert validate_email(data)
        assert validate_password(data)

        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)

            token = RefreshToken.for_user(user)
            data = serializer.data
            data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
            return Response(data, status=status.HTTP_200_OK)


class UserLogout(APIView):
    permission_classes = (AllowAny,)


    def post(self, request):
        logout(request)
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


    def get(self, request):
        serializer = UserSerializer(request.user)

        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
