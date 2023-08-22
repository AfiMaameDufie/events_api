from django.urls import path, include
from rest_framework import routers

from events.views import CategoryViewSet, EventViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'event', EventViewSet)


urlpatterns = [
    path('', include(router.urls)),
]