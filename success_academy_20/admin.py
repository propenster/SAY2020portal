from django.contrib import admin
from .models import LGA, DistrictGroup, Cluster, District, Participant

# Register your models here.

admin.site.register(LGA)
admin.site.register(DistrictGroup)
admin.site.register(Cluster)
admin.site.register(District)
admin.site.register(Participant)
