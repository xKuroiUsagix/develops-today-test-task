from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from spy_cat.models import SpyCat

from .models import Mission, Target
from .serializers import MissionSerializer, TargetSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()

        if mission.cat is not None:
            return Response(
                {'detail': 'You cannot delete a mission as it is assigned to a cat.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_destroy(mission)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['patch'])
    def assign_cat(self, request, *args, **kwargs):
        mission = self.get_object()
        cat_id = request.data.get('cat_id')

        if cat_id is None:
            return Response(
                {'detail': 'cat_id is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not SpyCat.objects.filter(id=cat_id).exists():
            return Response(
                {'detail': f'Cat with id {cat_id} does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        mission.cat = SpyCat.objects.get(id=cat_id)
        mission.save()

        return Response(
            {'detail': 'Cat assigned to mission successfully.'},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['patch'])
    def remove_cat(self, request, *args, **kwargs):
        mission = self.get_object()
        mission.cat = None
        mission.save()

        return Response(
            {'detail': 'Cat was removed from this mission.'},
            status=status.HTTP_200_OK
        )


    @action(detail=True, methods=['patch'])
    def update_target_notes(self, request, *args, **kwargs):
        mission = self.get_object()
        target_id = request.data.get('target_id')

        target_validation = self._validate_target(mission, target_id)
        if target_validation is not None:
            return target_validation

        if not request.data.get('notes'):
            return Response(
                {'detail': 'Field `notes` is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        target = mission.targets.get(id=target_id)

        if target.is_complete:
            return Response(
                {'detail': 'You cannot change notes for completed target.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        target.notes = request.data.get('notes')
        target.save()

        return Response(
            {'detail': 'Target\'s notes was updated successfully.'},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['patch'])
    def complete_target(self, request, *args, **kwargs):
        mission = self.get_object()
        target_id = request.data.get('target_id')

        target_validation = self._validate_target(mission, target_id)
        if target_validation is not None:
            return target_validation
        
        target = mission.targets.get(id=target_id)
        target.is_complete = True
        target.save()

        if not mission.targets.filter(is_complete=False).exists():
            mission.is_complete = True
            mission.save()

        return Response(
            {'detail': 'Target was marked as completed.'},
            status=status.HTTP_200_OK
        )

    
    def _validate_target(self, mission, target_id: int) -> Response:
        if target_id is None:
            return Response(
                {'detail': 'target_id is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        print(target_id, type(target_id))
        if not mission.targets.filter(id=target_id).exists():
            return Response(
                {'detail': 'This mission does not have requested target.'},
                status=status.HTTP_400_BAD_REQUEST
            )
