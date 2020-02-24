from django.db import models

# Create your models here.

class Device(models.Model):
    '''
    device 包含以下字段ip，dev_name，vendor（厂商），model（型号），series（系列）
    '''
    ip = models.CharField(verbose_name='IP', max_length=128)
    dev_name = models.CharField(verbose_name='Device_name', max_length=128)
    vendor = models.CharField(verbose_name='Vendor', max_length=128)
    model = models.CharField(verbose_name='Model', max_length=128)
    series = models.CharField(verbose_name='Series', max_length=128)

