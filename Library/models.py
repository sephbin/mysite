from django.db import models

# Create your models here.
class thingType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class thingSubType(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    
    def __str__(self):
        return self.name

class generalColour(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class supplier(models.Model):
    companyName = models.CharField(max_length=200)
    companyNumber = models.CharField(max_length=200, default="none provided")
    companyAddress = models.CharField(max_length=200)
    leadtime = models.CharField(max_length=200)

    def __str__(self):
        return self.companyName

class finishes(models.Model):
    finishestype = models.CharField(max_length=200)

    def __str__(self):
        return self.finishestype

class location(models.Model):
    locationtype = models.CharField(max_length=200)

    def __str__(self):
        return self.locationtype

class included(models.Model):
    includedtype = models.CharField(max_length=200)

    def __str__(self):
        return self.includedtype

class suitability(models.Model):
    suitabilitytype = models.CharField(max_length=200)

    def __str__(self):
        return self.suitabilitytype

class condition(models.Model):
    conditiontype = models.CharField(max_length=200)

    def __str__(self):
        return self.conditiontype

class assemblymethod(models.Model):
    assemblymethodtype = models.CharField(max_length=200)

    def __str__(self):
        return self.assemblymethodtype

class edges(models.Model):
    edgestype = models.CharField(max_length=200)

    def __str__(self):
        return self.edgestype

class materials(models.Model):
    materialstype = models.CharField(max_length=200)

    def __str__(self):
        return self.materialstype

class CSSS(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    CSSz = models.TextField(max_length=200)
    def __str__(self):
        return self.name


class thing(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(thingType, on_delete=models.SET_NULL, related_name="things", null=True )
    subType = models.ForeignKey(thingSubType, on_delete=models.SET_NULL, related_name="things", null=True)

    colour = models.CharField(max_length=200, blank=True, null=True)

    generalColour = models.ForeignKey(generalColour, on_delete=models.SET_NULL, related_name="things", null=True, blank=True)

    size = models.CharField(max_length=512, blank=True, null=True)

    supplier = models.ForeignKey(supplier, on_delete=models.SET_NULL, related_name="things", null=True)

    specialNimatBlock = models.FileField(blank=True, null=True)

    specialimageblock = models.FileField(blank=True, null=True)

    cost = models.CharField(max_length=512, blank=True, null=True)

    sustainability = models.CharField(max_length=512, blank=True, null=True)

    flamability = models.CharField(max_length=512, blank=True, null=True)

    sliprating = models.FloatField(blank=True, null=True)

    finishes= models.ForeignKey(finishes, on_delete=models.SET_NULL, related_name="things", null=True)

    timberfinishes = models.CharField(max_length=512, blank=True, null=True)

    metalfinishes = models.CharField(max_length=512, blank=True, null=True)

    glasstreatment = models.CharField(max_length=512, blank=True, null=True)

    metal = models.CharField(max_length=512, blank=True, null=True)

    metalaging = models.CharField(max_length=512, blank=True, null=True)

    metaltexture = models.CharField(max_length=512, blank=True, null=True)

    location = models.ForeignKey(location, on_delete=models.SET_NULL, related_name="things", null=True)

    included = models.ForeignKey(included, on_delete=models.SET_NULL, related_name="things", null=True)

    suitability = models.ForeignKey(suitability, on_delete=models.SET_NULL, related_name="things", null=True)

    condition = models.ForeignKey(condition, on_delete=models.SET_NULL, related_name="things", null=True)

    origin = models.CharField(max_length=512, blank=True, null=True)

    assemblymethod = models.ForeignKey(assemblymethod, on_delete=models.SET_NULL, related_name="things", null=True)

    transparency = models.CharField(max_length=512, blank=True, null=True)

    ISratings = models.CharField(max_length=512, blank=True, null=True)

    edges = models.ForeignKey(edges, on_delete=models.SET_NULL, related_name="things", null=True)

    materials = models.ForeignKey(materials, on_delete=models.SET_NULL, related_name="things", null=True)

    timber = models.CharField(max_length=512, blank=True, null=True)
    
    cutsofwood = models.CharField(max_length=512, blank=True, null=True)

    acousticdata = models.CharField(max_length=512, blank=True, null=True)

    thickness = models.CharField(max_length=512, blank=True, null=True)

    maximumweightcapacity = models.CharField(max_length=512, blank=True, null=True)

    careinstructions = models.CharField(max_length=512, blank=True, null=True)

    reflectionfactor = models.CharField(max_length=512, blank=True, null=True)

    productwarranty = models.CharField(max_length=512, blank=True, null=True)

    age = models.CharField(max_length=512, blank=True, null=True)

    overallproductweight = models.CharField(max_length=512, blank=True, null=True)

    CSSS = models.TextField(max_length=512, blank=True, null=True)


    def __str__(self):
        return self.name

    #http://localhost:8000/admin/Library/thing/1/change/