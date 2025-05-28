from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from desafio.models import Video
from desafio.serializers import VideoSerializer


class VideosViewSet(viewsets.ModelViewSet):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    

class ListaVideoUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'id'
    