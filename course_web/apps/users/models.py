from datetime import datetime

from django.db import models

# Create your models here.
from college.models import Classroom, Department

class Teacher(models.Model):
    '''教师表'''
    teacher_name = models.CharField(max_length=45, verbose_name='姓名')
    teacher_num = models.CharField(max_length=45, verbose_name='职工号')
    sex = models.CharField(max_length=6, choices=(('男', '男'), ('女', '女')), default='女', verbose_name='性别')
    department = models.ForeignKey(Department, verbose_name='系')
    phone = models.CharField(max_length=32, null=True, blank=True, verbose_name='电话')
    email = models.EmailField(null=True, blank=True, max_length=50, verbose_name='邮箱')
    picture = models.ImageField(null=True, blank=True, upload_to='static/teacher', verbose_name='头像')
    age = models.IntegerField(default=18, verbose_name='年龄' )
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'teacher_info'
        verbose_name = '教师信息'
        verbose_name_plural = "教师信息"

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField(max_length=45, verbose_name='姓名')
    student_num = models.CharField(max_length=45, unique=True, verbose_name='学号')
    classroom = models.ForeignKey(Classroom, verbose_name='班级')
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

class Users(models.Model):
    username = models.CharField(max_length=45, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    categroy = models.CharField(max_length=12, choices=(('学生', '学生'), ('教师', '教师')), default='学生', verbose_name='权限')
    name = models.CharField(max_length=45, verbose_name='姓名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'users_info'
        verbose_name = '登录信息'
        verbose_name_plural = "登录信息"

    def __str__(self):
        return self.username


