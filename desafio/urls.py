from django.urls import path, include
from rest_framework import routers

from desafio.views import VideosViewSet

# router = routers.DefaultRouter()
# router.register('videos', VideosViewSet, basename="Videos")

# urlpatterns = [
#     path('', router.urls),
# ]