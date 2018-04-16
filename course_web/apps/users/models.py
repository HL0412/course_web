from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from college.models import Classroom, Department

class Student(models.Model):
    student_name = models.CharField(max_length=45, verbose_name='姓名')
    student_num = models.CharField(max_length=45, unique=True, verbose_name='学号')
    classroom = models.ForeignKey(Classroom, verbose_name='班级', on_delete=models.CASCADE)
    sex = models.CharField(max_length=6, choices=(('男', '男'), ('女', '女')), default='女', verbose_name='性别')
    phone = models.CharField(max_length=32, null=True, blank=True,verbose_name='电话')
    email = models.EmailField(null=True, blank=True, max_length=50, verbose_name='邮箱')
    picture = models.ImageField(null=True, blank=True, default='image/default.png', upload_to='static/student', verbose_name='头像')
    age = models.IntegerField(default=18, verbose_name='年龄')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'student_info'
        verbose_name = '学生信息'
        verbose_name_plural = "学生信息"

    def __str__(self):
        return self.student_name

# class Users(models.Model):
#     username = models.CharField(max_length=45, verbose_name='用户名')
#     password = models.CharField(max_length=100, verbose_name='密码')
#     categroy = models.CharField(max_length=12, choices=(('学生', '学生'), ('教师', '教师')), default='学生', verbose_name='权限')
#     name = models.CharField(max_length=45, verbose_name='姓名')
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#     class Meta:
#         db_table = 'users_info'
#         verbose_name = '登录信息'
#         verbose_name_plural = "登录信息"
#
#     def __str__(self):
#         return self.username

class UserProfile(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女')
    )

    nick_name = models.CharField('昵称',max_length=50,default='')
    birthday = models.DateField('生日',null=True,blank=True)
    gender = models.CharField('性别',max_length=10,choices=gender_choices,default='female')
    adress = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register','注册'),
        ('forget','找回密码')
    )

    code = models.CharField('验证码',max_length=20)
    email = models.EmailField('邮箱',max_length=50)
    send_type = models.CharField(choices=send_choices,max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'email'
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


