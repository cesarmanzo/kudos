from django.contrib.auth import get_user_model
from .models import Organization, Kudo, UserData
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['url', 'created_at', 'name', 'logo']

class KudoPostSerializer(serializers.ModelSerializer):
    # sent_by = serializers.StringRelatedField(many=False)
    # sent_to = serializers.StringRelatedField(many=False)
    class Meta:
        model = Kudo
        fields = ['sent_by', 'sent_to', 'message']

class KudoSerializer(serializers.ModelSerializer):
    sent_by = UserSerializer(many=False)
    sent_to = UserSerializer(many=False)
    class Meta:
        model = Kudo
        fields = ['url', 'created_at', 'sent_by', 'sent_to', 'message']

class UserDataSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = UserData
        ordering = ['-id']
        fields = ['url', 'organization', 'kudos_available', 'user', 'id']
