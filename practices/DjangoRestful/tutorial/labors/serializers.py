from django.forms import widgets
from rest_framework import serializers
from labors.models import Labor

class LaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labor
        fields = ('id', 'name', 'sex', 'job', 'IDCard', 'contactWay', 'notes')
        
