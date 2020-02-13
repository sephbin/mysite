from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views
router = routers.DefaultRouter()
router.register(r'things',		views.ThingViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls')),
]