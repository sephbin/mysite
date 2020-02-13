from .models import *
from rest_framework import serializers
from django.shortcuts import get_object_or_404

class ThingSerializer(serializers.ModelSerializer):
	class Meta:
		model = thing
		fields = ('__all__')


class ThingSerializer_JustName(serializers.ModelSerializer):
	class Meta:
		model = thing
		fields = ('name',)
