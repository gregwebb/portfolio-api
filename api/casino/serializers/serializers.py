from django.conf import settings
from rest_framework import serializers
from ..models import Profile
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

class NDASerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = (
            'email',
            'is_staff',
            'firebase_id',
            'user_type',
        )
