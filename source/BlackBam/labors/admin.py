#coding=utf-8#

from django.contrib import admin
from BlackBam.labors.models import Department, Labor, Attendance, Salary, SalaryStatement

admin.site.register(Department)
admin.site.register(Labor)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(SalaryStatement)
