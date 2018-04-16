from datetime import datetime
from django.db import models
from college.models import Department
# Create your models here.


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

class Course(models.Model):

    course_name = models.CharField(max_length=45, verbose_name=u"课程名")
    course_num = models.IntegerField(unique=True, verbose_name=u"课程号")
    course_intro = models.TextField(null=True, blank=True, verbose_name='课程介绍')
    course_picture = models.ImageField(null=True, blank=True, upload_to='static/course/image', default='static/image/default.png', max_length=100, verbose_name='课程图片')
    course_teacher = models.ManyToManyField(Teacher, verbose_name='课程教师')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'course_info'
        verbose_name = '课程信息'
        verbose_name_plural = "课程信息"

    def __str__(self):
        return self.course_name

class Video(models.Model):

    course = models.ForeignKey(Course, verbose_name='课程名', on_delete=models.CASCADE)
    video_name = models.CharField(max_length=100, verbose_name='视频名')
    url = models.URLField(max_length=150, verbose_name='视频地址')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长（分钟数)')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'course_video'
        verbose_name = '课程视频'
        verbose_name_plural = '课程视频'

    def __str__(self):
        return self.video_name

class Data(models.Model):

    course = models.ForeignKey(Course, verbose_name='课程名', on_delete=models.CASCADE)
    data_name = models.CharField(max_length=100, verbose_name='资料名称')
    data = models.FileField(upload_to='static/course/data', verbose_name='课程资料', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'course_data'
        verbose_name = '课程资料'
        verbose_name_plural = '课程资料'

    def __str__(self):
        return self.data_name

class PPT(models.Model):

    course = models.ForeignKey(Course, verbose_name='课程名', on_delete=models.CASCADE)
    ppt_name = models.CharField(max_length=100, verbose_name='课件名称')
    ppt = models.FileField(upload_to='static/course/ppt', verbose_name='课件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'course_ppt'
        verbose_name = '课件'
        verbose_name_plural = '课件'

    def __str__(self):
        return self.ppt_name

