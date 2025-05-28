from django.contrib import admin

from desafio.models import Video


@admin.register(Video)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'url')
    list_display_links = ('id', 'titulo',)
    list_per_page = 20
    search_fields = ['titulo']
    