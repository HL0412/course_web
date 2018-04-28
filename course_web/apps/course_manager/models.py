from datetime import datetime
from django.db import models
from college.models import Teacher
# Create your models here.


class Course(models.Model):

    name = models.CharField(max_length=45, verbose_name=u"课程名")
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

