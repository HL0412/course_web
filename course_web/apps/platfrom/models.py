from datetime import datetime

from django.db import models

# Create your models here.
from course_manager.models import Course
from users.models import Student, Teacher


class Notice(models.Model):

    title = models.CharField(max_length=45, verbose_name='题目')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    content = models.TextField(verbose_name='内容', max_length=100)
    picture = models.ImageField(null=True, blank=True, upload_to='static/notice', default='image/default.png', max_length=100, verbose_name='图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'notice_info'
        verbose_name = '公告管理'
        verbose_name_plural = "公告管理"

    def __str__(self):
        return self.title

class News(models.Model):

    title = models.CharField(max_length=45, verbose_name='题目')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    content = models.TextField(verbose_name='内容', max_length=100)
    picture = models.ImageField(null=True, blank=True, upload_to='static/news', default='image/default.png', max_length=100, verbose_name='图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'news_info'
        verbose_name = '新闻管理'
        verbose_name_plural = "新闻管理"

    def __str__(self):
        return self.title

class Work(models.Model):
    student = models.ForeignKey(Student, verbose_name='学生')
    course = models.ForeignKey(Course, verbose_name='课程名')
    teacher = models.ForeignKey(Teacher, verbose_name='教师')
    title = models.CharField(max_length=45, verbose_name='作业题目')
    content = models.FileField(upload_to='static/work', verbose_name='作业内容', max_length=100)
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='提交时间')
    class Meta:
        db_table = 'work_info'
        verbose_name = '学生作业管理'
        verbose_name_plural = "学生作业管理"

    def __str__(self):
        return self.title

class WorkPublish(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程名')
    teacher = models.ForeignKey(Teacher, verbose_name='教师')
    title = models.CharField(max_length=45, verbose_name='作业题目')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    class Meta:
        db_table = 'work_publish_info'
        verbose_name = '作业发布管理'
        verbose_name_plural = "作业发布管理"

    def __str__(self):
        return self.title


