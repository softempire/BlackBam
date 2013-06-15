#coding=utf-8#

from django.contrib import admin
from BlackBam.labors.models import Department, Labor, Attendance, Salary, SalaryStatement


#Department
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    search_fields = ('name', 'project')
    list_filter = ('project',)
    ordering = ('name',)

admin.site.register(Department, DepartmentAdmin)


#Labor
class LaborAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'job', 'IDCard', 'contact', 'notes',)
    search_fields = ('name', 'IDCard',)
    list_filter = ('name', 'sex', 'job',)
    ordering = ('name', 'sex', 'job')

admin.site.register(Labor, LaborAdmin)


admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(SalaryStatement)
