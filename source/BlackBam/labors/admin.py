#coding=utf-8#

from django.contrib import admin
from BlackBam.labors.models import Department, Labor, Attendance, Salary, SalaryStatement

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    search_fields = ('name', 'project')
    list_filter = ('project',)
    ordering = ('name',)

admin.site.register(Department, DepartmentAdmin)

admin.site.register(Labor)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(SalaryStatement)
