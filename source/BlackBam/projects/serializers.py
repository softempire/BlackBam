#coding=utf-8#

from django.forms import widgets
from rest_framework import serializers
from BlackBam.projects.models import Project
from BlackBam.labors.serializers import DepartmentSerializer

class ProjectSerializer(serializers.ModelSerializer):
#    departments = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Project
        fields = ('name', 'address', 'year')
        
