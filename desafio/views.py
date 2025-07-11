from rest_framework import viewsets
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404
from desafio.models import Video, Categoria
from desafio.serializers import VideoSerializer, CategoriaSerializer


class VideosViewSet(viewsets.ModelViewSet):

    serializer_class = VideoSerializer
    filterset_fields = ['titulo', 'url']
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Video.objects.all()


class CategoriasViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.all()

    def get_object(self):
        try:
            return super().get_object()
        except Exception as e:
            raise NotFound(detail="Não encontrado")


class ListaVideosPorCategoria(generics.ListAPIView):

    serializer_class = VideoSerializer

    def get_queryset(self):
        id_categoria = self.kwargs.get('pk')

        try:
            categoria = get_object_or_404(Categoria, pk=id_categoria)
        except:
            raise NotFound(detail="Não encontrado")

        return Video.objects.filter(categoria=categoria)
