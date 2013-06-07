#coding=utf-8#

from rest_framework import serializers
from BlackBam.labors.models import Department, Labor, Attendance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        field = ('name', 'project')

class LaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labor
        fields = ('id', 'name', 'sex', 'job', 'IDCard', 'contact', 'notes')
        
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id', 'labor', 'year', 'month', 'attend')