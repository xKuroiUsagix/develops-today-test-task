from rest_framework import serializers

from .models import SpyCat


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['name', 'experience', 'breed', 'salary']
