from django.shortcuts import redirect
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .models import *

class SuvViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer

class MijozViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer

class AdminAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        admin = Admin.objects.all()
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)

class AdminDetailAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        model = Admin.objects.get(id=pk)
        serializer = AdminSerializer(model)
        return Response(serializer.data)


class BuyurtmaAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        model = Buyurtma.objects.all()
        serializer = BuyurtmaSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        buyurtma = request.data
        serializer = BuyurtmaSerializer(data=buyurtma)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuyurtmaDetailAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        model = Buyurtma.objects.get(id=pk)
        serializer = BuyurtmaSerializer(model)
        return Response(serializer.data)

class HaydovchiAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        admin = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(admin, many=True)
        return Response(serializer.data)

class HaydovchiDetailAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        model = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(model)
        return Response(serializer.data)