from django.test import TestCase
from django.core.exceptions import ValidationError

from desafio.models import Video, Categoria
from desafio.serializers import CategoriaSerializer

class TestVideoModel(TestCase):
    
    def setUp(self):
        self.categoria = Categoria.objects.create()

    def test_create_video_valid(self):
        video = Video.objects.create(
        titulo='Pearl Jam - Black (Official Audio)',
        descricao='Descrição teste',
        url='https://exemplo.com/default/',
        categoria=self.categoria,
        )

        self.assertEqual(video.titulo, 'Pearl Jam - Black (Official Audio)')
        self.assertEqual(video.descricao, 'Descrição teste')
        self.assertEqual(video.url, 'https://exemplo.com/default/')
        self.assertEqual(video.categoria, self.categoria)
    
    def test_create_video_whithout_categoria(self):
        video = Video.objects.create(
        titulo='Pearl Jam - Black (Official Audio)',
        descricao='Descrição teste',
        url='https://exemplo.com/default/',
        )

        self.assertEqual(video.categoria.titulo, 'livre')

    def test_titulo_cant_be_empty(self):
        """Verifica se o sistema rejeita títulos vazios"""
        with self.assertRaises(ValidationError):
            video = Video.objects.create(
                titulo='',
                descricao='Descrição teste',
                url='https://exemplo.com/default/',
                categoria=self.categoria,
            )
