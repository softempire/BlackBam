#coding=utf-8#

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
    name = models.CharField(max_length=20, blank=False, verbose_name='姓名')
    sex = models.BooleanField(default=True, verbose_name='男')
    job = models.CharField(max_length=200, verbose_name='职务')
    IDCard = models.CharField(max_length=50, verbose_name='身份证')
    contact = models.CharField(max_length=300, verbose_name='联系方式')
    notes = models.CharField(max_length=500, verbose_name='备注')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'


#出勤
class Attendance(models.Model):
    labor = models.ForeignKey(Labor, verbose_name='员工')
    year = models.IntegerField(verbose_name='年份')
    month = models.IntegerField(verbose_name='月份')
    attend = models.CommaSeparatedIntegerField(max_length=100, verbose_name='出勤')

    def __unicode__(self):
        return "Attendance_" + self.labor.name + str(self.year) + str(self.month)

    class Meta:
        verbose_name = '出勤'
        verbose_name_plural = '出勤'


#工资
class Salary(models.Model):
    labor = models.ForeignKey(Labor, verbose_name='员工')
    year = models.IntegerField(verbose_name='年份')
    month = models.IntegerField(verbose_name='月份')
    salary = models.IntegerField(verbose_name='应发工资')
    actualSalary = models.IntegerField(verbose_name='实发工资')

    def __unicode__(self):
        return "工资_" + self.labor.name + str(self.year) + str(self.month)

    class Meta:
        verbose_name = '工资'
        verbose_name_plural = '工资'

#工资出账单
class SalaryStatement(models.Model):
    labor = models.ForeignKey(Labor, verbose_name='员工')
    arriveDate = models.DateField(verbose_name='到班组时间')
    leaveDate = models.DateField(verbose_name='离开班组时间')
    attachment = models.CharField(max_length=500, verbose_name='附件')
    notes = models.CharField(max_length=500, verbose_name='备注')

    def __unicode__(self):
        return "工资出账单_" + self.labor.name

    class Meta:
        verbose_name = '工资出账单'
        verbose_name_plural = '工资出账单'