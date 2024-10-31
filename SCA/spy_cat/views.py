from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import SpyCat
from .serializers import SpyCatSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        allowed_feild = 'salary'

        if allowed_feild not in request.data.keys():
            return Response(
                {'detail': f'Only `salary` field allowed to be modified.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        instance.salary = request.data.get(allowed_feild)
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
