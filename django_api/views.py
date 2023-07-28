from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django_api.serializers import UserRegisterSerializers,UserLoginSerializer,UserLogoutSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics,permissions


#Generating Tokens manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



# Create your views here.
class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegisterSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            tokens=get_tokens_for_user(user)
            return Response({'tokens':tokens,'msg':'Registration Successful'})
        return Response(serializer.errors)
    





class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            contact=serializer.data.get('contact')
            password=serializer.data.get('password')
            user=authenticate(contact=contact,password=password)
            if user is not None:
                tokens=get_tokens_for_user(user)
                return Response({'tokens':tokens,'msg':'you are logged in'})
            
            else:
                return Response({'error':{'non_field_error':["Your contact number or password doesn't match"]}})
        return Response(serializer.errors)
        



class UserLogoutView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer=UserLogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Token blacklisted successfully."}, status=status.HTTP_200_OK)


