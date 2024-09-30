from django.urls import path
from rest_framework import routers

from .views import FaceView, AgentView, DivisionView

app_name = 'agents'

router = routers.SimpleRouter()
router.register('divisions', DivisionView, basename='division')
router.register('faces', FaceView, basename='face')
router.register('agents', AgentView, basename='agent')


urlpatterns = router.urls
