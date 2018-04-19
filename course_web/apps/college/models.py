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
    department =  models.ForeignKey(Department, verbose_name='系名', on_delete=models.CASCADE)
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

class Teacher(models.Model):

    '''教师表'''
    teacher_name = models.CharField(max_length=45, verbose_name='姓名')
    teacher_num = models.CharField(max_length=45, verbose_name='职工号')
    sex = models.CharField(max_length=6, choices=(('男', '男'), ('女', '女')), default='女', verbose_name='性别')
    department = models.ForeignKey(Department, verbose_name='系', on_delete=models.CASCADE)
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