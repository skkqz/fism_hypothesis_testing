from django.urls import path
from rest_framework import routers

from .views import FaceView, AgentView, DivisionView, AgentAgreementsView

app_name = 'app_agents'

router = routers.SimpleRouter()
router.register('divisions', DivisionView, basename='division')
router.register('faces', FaceView, basename='face')
router.register('agents', AgentView, basename='agent')
router.register('agents_agreements', AgentAgreementsView, basename='agents_agreements')


urlpatterns = router.urls
