from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views
router = routers.DefaultRouter()
router.register(r'things',		views.ThingViewSet)

urlpatterns = [
	path(r'choosething/<str:thingtype>/<str:srating>/<str:gcolour>/<str:choice>/', views.getOneThing),

	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls')),
]