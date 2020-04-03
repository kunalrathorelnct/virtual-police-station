from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(DocumentVerification)
admin.site.register(FIRDetail)
admin.site.register(PoliceStationDetail)
admin.site.register(OTPVerification)
admin.site.register(CyberCrime)
#admin.site.register(WitnessDetail)
