from django.conf.urls import patterns, include, url

from BlackBam.labors.views import LaborList, LaborDetail, AttendanceList, SalaryList, SalaryStatementList
from BlackBam.labors.views import DepartmentList, DepartmentDetail, AttendanceDetail, SalaryDetail, SalaryStatementDetail


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/department_list/$', DepartmentList.as_view()),
    url(r'^api/labor_list/$', LaborList.as_view()),
    url(r'^api/attendance_list/$', AttendanceList.as_view()),
    url(r'^api/salary_list/$', SalaryList.as_view()),
    url(r'^api/salaryStatement_list/$', SalaryStatementList.as_view()),
)
