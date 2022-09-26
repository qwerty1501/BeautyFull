from rest_framework import serializers
from .models import Master, Services, Request
        
        
class MasterSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Master
        fields = ('id', 'name', 'picture', 'information', 'experience', 'position')


class ServicesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ('id', 'title', 'master')


class RequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Request
        fields = ('master', 'time', 'data', 'services', 'name', 'phone', 'sms', 'id')