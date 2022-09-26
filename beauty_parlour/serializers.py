from rest_framework import serializers
from .models import Master, Services, Request
        
        
class MasterSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Master
        fields = ('id', 'name_ky','name_en', 'name_ru' 'picture', 'information_ky', 'information_en', 'information_ru', 'experience_ky', 'experience_en', 'experience_ru', 'position_ky', 'position_en', 'position_ru')


class ServicesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ('id', 'title_ky', 'title_en', 'title_ru', 'master')


class RequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Request
        fields = ('master_ky', 'master_en', 'master_ru', 'time_ky', 'time_en', 'time_ru', 'data_ky', 'data_en', 'data_ru', 'services_ky', 'services_en', 'services_ru', 'name_ky', 'name_en', 'name_ru', 'phone', 'sms_ky', 'sms_en', 'sms_ru', 'id')