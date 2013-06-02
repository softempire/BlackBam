#coding=utf-8#

from django.forms import widgets
from rest_framework import serializers
from BlackBam.labors.models import Department,Labor

class DepartmentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Department
        field = ('name', 'project')

class LaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labor
        fields = ('id', 'name', 'sex', 'job', 'IDCard', 'contactWay', 'notes')
        
