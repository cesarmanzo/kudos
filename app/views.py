from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Organization, Kudo, UserData
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by('-created_at')
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]


class KudoViewSet(viewsets.ModelViewSet):
    queryset = Kudo.objects.all().order_by('-created_at')
    serializer_class = KudoSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all().order_by('-id')
    serializer_class = UserDataSerializer
    permission_classes = [permissions.IsAuthenticated]



