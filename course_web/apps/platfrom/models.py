from datetime import datetime
from django.db import models
from course_manager.models import Course, Teacher
from college.models import Student

# Create your models here.

class Notice(models.Model):

    title = models.CharField(max_length=45, verbose_name='题目')
    introduction = models.CharField(max_length=100, verbose_name='简介')
    content = models.TextField(verbose_name='内容')
    picture = models.ImageField(null=True, blank=True, upload_to='static/notice', default='image/default.png', max_length=100, verbose_name='图片')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    class Meta:
        db_table = 'notice_info'
        verbose_name = '公告管理'
        verbose_name_plural = "公告管理"

    def __str__(self):
        return self.title

class News(models.Model):

    title = models.CharField(max_length=45, verbose_name='题目')
    introduction = models.CharField(max_length=100, verbose_name='简介')
    content = models.TextField(verbose_name='内容'),
    picture = models.ImageField(null=True, blank=True, upload_to='static/news', default='image/default.png', max_length=100, verbose_name='图片')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    class Meta:
        db_table = 'news_info'
        verbose_name = '新闻管理'
        verbose_name_plural = "新闻管理"

    def __str__(self):
        return self.title

class WorkCommit(models.Model):
    student = models.ForeignKey(Student, verbose_name='学生', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程名', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='教师', on_delete=models.CASCADE)
    title = models.CharField(max_length=45, verbose_name='作业题目')
    content = models.FileField(upload_to='static/work', verbose_name='作业内容', max_length=100)
    commit_time = models.DateTimeField(default=datetime.now, verbose_name='提交时间')
    class Meta:
        db_table = 'work_commit'
        verbose_name = '学生作业管理'
        verbose_name_plural = "学生作业管理"

    def __str__(self):
        return self.title

class WorkPublish(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程名', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='教师', on_delete=models.CASCADE)
    title = models.CharField(max_length=45, verbose_name='作业题目')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    class Meta:
        db_table = 'work_publish'
        verbose_name = '作业发布管理'
        verbose_name_plural = "作业发布管理"

    def __str__(self):
        return self.title


