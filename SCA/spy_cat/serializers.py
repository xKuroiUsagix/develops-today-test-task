from rest_framework import serializers

from .models import SpyCat


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'experience', 'breed', 'salary']
        read_only_fields = ['id']
