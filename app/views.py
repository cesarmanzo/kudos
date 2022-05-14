# from django.shortcuts import render

from django.contrib.auth import get_user_model
from .models import Organization, Kudo, UserData
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


User = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.order_by('-created_at')
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(organization=self.request.user.organization)
        return qs

class UsersAvailableViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.order_by('id')
    serializer_class = UserDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_org = UserData.objects.get(user=self.request.user)
        qs = UserData.objects.filter(organization=user_org.organization).exclude(user=user_org.user.id)
        return qs

class KudoSentViewSet(viewsets.ModelViewSet):
    queryset = Kudo.objects.all().order_by('-created_at')
    serializer_class = KudoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(sent_by=self.request.user)
        return qs


@api_view(['POST'])
def kudos_post(request):
    request.data['sent_to'] = int(request.data['sent_to'])
    request.data['sent_by'] = User.objects.get(username=request.user).id
    serializer = KudoPostSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        userdata = UserData.objects.get(user=request.user)
        if userdata.kudos_available >= 1:
            serializer.save()
            userdata.kudos_available = userdata.kudos_available-1
            userdata.save()
            return Response(serializer.data)
        else:
            return Response('Less than 1 kudo')
    else:
        return Response('Invalid Serializer')



class KudoReceivedViewSet(viewsets.ModelViewSet):
    queryset = Kudo.objects.all().order_by('-created_at')
    serializer_class = KudoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(sent_to=self.request.user)
        return qs


class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.order_by('-id')
    serializer_class = UserDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class MyInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

