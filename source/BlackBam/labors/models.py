#coding=utf-8#

from datetime import date
from django.db import models
from BlackBam.projects.models import Project


#部门
class Department(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name='名称')
    project = models.ForeignKey(Project, verbose_name='工程')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '班组'
        verbose_name_plural = '班组'


#员工
class Labor(models.Model):
    name = models.CharField(max_length=20, blank=False)
    sex = models.BooleanField()
    job = models.CharField(max_length=200)
    IDCard = models.CharField(max_length=50)
    contact = models.CharField(max_length=300)
    notes = models.CharField(max_length=500)

    def __unicode__(self):
        return "Labor_" + self.name


#出勤
class Attendance(models.Model):
    labor = models.ForeignKey(Labor)
    year = models.IntegerField()
    month = models.IntegerField()
    attend = models.CommaSeparatedIntegerField(max_length=100)

    def __unicode__(self):
        return "Attendance_" + self.labor.name + str(self.year) + str(self.month)


#工资
class Salary(models.Model):
    labor = models.ForeignKey(Labor)
    year = models.IntegerField()
    month = models.IntegerField()
    salary = models.IntegerField()
    actualSalary = models.IntegerField()

    def __unicode__(self):
        return "Salary_" + self.labor.name + str(self.year) + str(self.month)


#工资出账单
class SalaryStatement(models.Model):
    labor = models.ForeignKey(Labor)
    arriveDate = models.DateField()
    leaveDate = models.DateField()
    attachment = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)

    def __unicode__(self):
        return "SalaryStatement_" + self.labor.name