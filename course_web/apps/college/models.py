from datetime import datetime
from django.db import models

# Create your models here.

class Department(models.Model):
    department_name = models.CharField(max_length=100, verbose_name='系名')
    number = models.IntegerField(unique=True, verbose_name='系编号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'department_info'
        verbose_name = '系别信息'
        verbose_name_plural = '系别信息'

    def __str__(self):
        return self.department_name

class Classroom(models.Model):
    department =  models.ForeignKey(Department, verbose_name='系名')
    grade = models.CharField(max_length=45, verbose_name='年级')
    major =models.CharField(max_length=45,  verbose_name='专业')
    classes = models.IntegerField(unique=True, verbose_name='班号', default=1)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'classroom_info'
        verbose_name = '班级信息'
        verbose_name_plural = "班级信息"

    def __str__(self):
        return self.major