from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(thing)
admin.site.register(thingType)
admin.site.register(thingSubType)
admin.site.register(supplier)
admin.site.register(finishes)
admin.site.register(location)
admin.site.register(included)
admin.site.register(suitability)
admin.site.register(condition)
admin.site.register(assemblymethod)
admin.site.register(edges)
admin.site.register(materials)
admin.site.register(CSSS)
admin.site.register(generalColour)

#admin.site.register(thickness)
#admin.site.register(maximumweightcapacity)
#admin.site.register(careinstructions)
#admin.site.register(age)
#admin.site.register(reflectionfactor)
#admin.site.register(productwarranty)
#admin.site.register(overallproductweight)

