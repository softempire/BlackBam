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

#Attendance
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('labor', 'year', 'month', 'attend',)
    search_fields = ('labor', 'year', 'month',)
    list_filter = ('labor', 'year', 'month',)
    ordering = ('labor', 'year', 'month',)

admin.site.register(Attendance, AttendanceAdmin)

#Salary
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('labor', 'year', 'month', 'salary', 'actualSalary',)
    search_fields = ('labor', 'year', 'month',)
    list_filter = ('labor', 'year', 'month',)
    ordering = ('labor', 'year', 'month',)

admin.site.register(Salary, SalaryAdmin)

#SalaryStatement
class SalaryStatementAdmin(admin.ModelAdmin):
    list_display = ('labor', 'arriveDate', 'leaveDate', 'attachment', 'notes',)
    search_fields = ('labor', 'arriveDate', 'leaveDate',)
    list_filter = ('labor', 'arriveDate', 'leaveDate',)
    ordering = ('labor', 'arriveDate', 'leaveDate',)
admin.site.register(SalaryStatement, SalaryStatementAdmin)
