from django.contrib.auth.models import User
from .models import Organization, Kudo, UserData
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ['url', 'created_at', 'name', 'logo']

class KudoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kudo
        fields = ['url', 'created_at', 'sent_by', 'sent_to', 'message']

class UserDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserData
        fields = ['url', 'user', 'organization', 'kudos_available']
