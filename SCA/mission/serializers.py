from rest_framework import serializers

from .models import Mission, Target


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_complete']
        read_only_feilds = ['id']


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'targets', 'is_complete']
        read_only_feilds = ['id', 'is_complete']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)

        targets = []
        for target in targets_data:
            targets.append(Target(mission=mission, **target))
        
        Target.objects.bulk_create(targets)

        return mission
