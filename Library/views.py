from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
# Create your views here.
class ThingViewSet(viewsets.ModelViewSet):
	queryset = thing.objects.all()
	serializer_class = ThingSerializer_JustName
	filter_backends = [filters.SearchFilter , DjangoFilterBackend]
	filterset_fields = ["generalColour__name",]
	search_fields = ("name",)


def getOneThing(reguest, thingtype, srating, gcolour, choice)

	thingtype = get_object_or_404(thingSubType, name=thingtype)
	gcolour = get_object_or_404(generalColour, name=gcolour)
	choicething = thing.objects.filter(subType = thingtype, sliprating__gte = float(srating), generalColour = gcolour).order_by(choice).last()
	return JsonResponse(ThingSerializer_JustName(choicething).data)