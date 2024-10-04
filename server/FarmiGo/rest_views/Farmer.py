from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from FarmiGo.models import Farmer
from FarmiGo.serializers import FarmerSerializer

class FarmerRest(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = Farmer.objects.all()
            serializer = FarmerSerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        name = request.data.get('name')
        age = request.data.get('age')
        phone = request.data.get('phone')
        aadhar_number = request.data.get('aadhar_number')
        address = request.data.get('address')

        if not all([name, age, phone, aadhar_number, address]):
            return Response({"Error": "Missing certain field. Please check the fields"}, status=status.HTTP_400_BAD_REQUEST)

        if Farmer.objects.filter(aadhar_number=aadhar_number).exists():
            return Response({"Error": "Farmer already exists"}, status=status.HTTP_400_BAD_REQUEST)

        farmer = Farmer(name=name, age=age, phone=phone, aadhar_number=aadhar_number, address=address)
        farmer.save()

        serializer = FarmerSerializer(farmer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, *args, **kwargs):
        id = request.data.get('id')

        if not id:
            return Response({"error": "Id is not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            farmer = Farmer.objects.get(id=id)
        except Farmer.DoesNotExist:
            return Response({"error": "Farmer not found"}, status=status.HTTP_404_NOT_FOUND)

        if request.data.get('name'):
            farmer.name = request.data.get('name')
        if request.data.get('age'):
            farmer.age = request.data.get('age')
        if request.data.get('phone'):
            farmer.phone = request.data.get('phone')
        if request.data.get('aadhar_number'):
            farmer.aadhar_number = request.data.get('aadhar_number')
        if request.data.get('address'):
            farmer.address = request.data.get('address')

        farmer.save()

        response_data = FarmerSerializer(farmer).data
        return Response(response_data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        try:
            farmer_id = request.data.get('id')

            if not farmer_id:
                return Response({"error": "Missing 'id' in the request body"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                farmer = Farmer.objects.get(id=farmer_id)
            except Farmer.DoesNotExist:
                return Response({"error": "Farmer not found"}, status=status.HTTP_404_NOT_FOUND)

            farmer.delete()
            return Response({"message": "Farmer successfully deleted"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
