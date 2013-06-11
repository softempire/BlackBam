#coding=utf-8#

from rest_framework import serializers
from BlackBam.labors.models import Department, Labor, Attendance, Salary, SalaryStatement

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

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ('id', 'labor', 'year', 'month', 'salary', 'actualSalary')

class SalaryStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryStatement
        fields = ('id', 'labor', 'arriveDate', 'leaveDate', 'attachment', 'notes')