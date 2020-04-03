from rest_framework import serializers
from .models import *


class FIRDetailSerializer(serializers.ModelSerializer):
    #police_station = serializers.SlugRelatedField(queryset = PoliceStationDetail.objects.all(),slug_field = 'station_name')
    class Meta:
        model = FIRDetail
        fields = '__all__' 
        read_only_fields = ['passed_to_CCTNS','police_station','complete']
        # extra_kwargs = {
        #     'slug': {'validators': []},
        # }


#############
class PoliceStationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStationDetail
        fields = ['station_name','phone_no',]
        
        
class DocumentVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentVerification
        fields = '__all__'
        read_only_fields = ['verified','process_complete']

# class WitnessDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = WitnessDetail
#         fields = '__all__'

class CyberCrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CyberCrime
        fields = '__all__'
        read_only_fields = ['passed_to_CC','complete']