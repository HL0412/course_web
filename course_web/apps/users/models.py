from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from college.models import Classroom, Department

class UserProfile(AbstractUser):

    gender_choices = (
        ('男','男'),
        ('女','女')
    )
    rank_choices =(
        ('学生','学生'),
        ('教师', '教师')
    )

    nick_name = models.CharField('昵称',max_length=50,default='')
    birthday = models.DateField('生日',null=True,blank=True)
    gender = models.CharField('性别',max_length=10,choices=gender_choices,default='女')
    adress = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,null=True,blank=True)
    # rank = models.CharField('权限',max_length=45, choices=rank_choices,default='学生')
    image = models.ImageField(upload_to='images/%Y/%m',default='image/default.png',max_length=100)

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    send_choices = (
        ('注册','注册'),
        ('注册','找回密码')
    )

    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'email'
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


