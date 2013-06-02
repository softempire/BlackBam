#coding=utf-8#

from django.db import models

#员工
class Labor(models.Model):
    name = models.CharField(max_length=20, blank=False)
    sex = models.BooleanField()
    job = models.CharField(max_length=200)
    IDCard = models.CharField(max_length=50)
    contactWay = models.CharField(max_length=300)
    notes = models.CharField(max_length=500)

    def __unicode__(self):
        return "Labor_" + self.name
