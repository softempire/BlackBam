#coding=utf-8#

from django.db import models

#项目
class Project(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name='名称')
    address = models.CharField(max_length=200, verbose_name='地址')
    year = models.IntegerField(verbose_name='年份')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '工程'
        verbose_name_plural = '工程'

	