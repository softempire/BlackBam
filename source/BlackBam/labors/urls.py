from django.conf.urls import patterns, include, url
from BlackBam.labors.views import DepartmentList, DepartmentDetail, AttendanceDetail
from BlackBam.labors.views import LaborList, LaborDetail, AttendanceList

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/department_list/$', DepartmentList.as_view()),
    url(r'^api/labor_list/$', LaborList.as_view()),
    url(r'^api/attendance_list/$', AttendanceList.as_view()),
)
