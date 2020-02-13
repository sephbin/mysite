from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class ThingViewSet(viewsets.ModelViewSet):
	queryset = thing.objects.all()
	serializer_class = ThingSerializer_JustName
	filter_backends = [filters.SearchFilter , DjangoFilterBackend]
	filterset_fields = ["generalColour__name",]
	search_fields = ("name",)