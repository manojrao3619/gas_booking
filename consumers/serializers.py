from rest_framework import serializers
from .models import Profile

class ConsumerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

