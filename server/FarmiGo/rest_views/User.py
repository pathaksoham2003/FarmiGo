from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from FarmiGo.models import User
from FarmiGo.serializers import UserSerializer
from django.contrib.auth.hashers import make_password  # Import for password hashing

class UserRest(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')  # This should be hashed before storing

        if not all([name, email, password]):
            return Response({"Error": "Missing certain fields. Please check the fields"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"Error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Hash the password before saving
        hashed_password = make_password(password)

        user = User(name=name, email=email, password=hashed_password)
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        id = request.data.get('id')

        if not id:
            return Response({"error": "Id is not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.data.get('name'):
            user.name = request.data.get('name')
        if request.data.get('email'):
            user.email = request.data.get('email')
        if request.data.get('password'):
            user.password = make_password(request.data.get('password'))  # Re-hash new password if changed

        user.save()

        response_data = UserSerializer(user).data
        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        try:
            user_id = request.data.get('id')

            if not user_id:
                return Response({"error": "Missing 'id' in the request body"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            user.delete()
            return Response({"message": "User successfully deleted"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
