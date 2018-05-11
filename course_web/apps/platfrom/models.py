from datetime import datetime
from django.db import models

from college.models import Classroom
from course_manager.models import Course, Student, Teacher


# Create your models here.

class Notice(models.Model):

    title = models.CharField(max_length=45, verbose_name='题目')
    introduction = models.CharField(max_length=100, verbose_name='简介')
    content = models.TextField(verbose_name='内容')
    picture = models.ImageField(null=True, blank=True, upload_to='notice/%Y/%m', default='image/default.png', max_length=100, verbose_name='图片')
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
    content = models.TextField(verbose_name='内容')
    picture = models.ImageField(null=True, blank=True, upload_to='news/%Y/%m', default='image/default.png', max_length=100, verbose_name='图片')
    publish_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')
    class Meta:
        db_table = 'news_info'
        verbose_name = '新闻管理'
        verbose_name_plural = "新闻管理"

    def __str__(self):
        return self.title

class WorkCommit(models.Model):
    GRADE_CHOICES = (

        ("freshman", u"大一"),
        ("sophomore", u"大二"),
        ("junior", u"大三"),
        ("senior", u"大四"),

    )
    student = models.ForeignKey(Student, verbose_name='学生', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程名', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name='教师', on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, verbose_name='班级', on_delete=models.CASCADE)
    grade = models.CharField(max_length=45, choices=GRADE_CHOICES, verbose_name='年级', default="freshman")
    title = models.CharField(max_length=45, verbose_name='作业题目')
    content = models.FileField(upload_to='work/content/%Y/%m', verbose_name='作业内容', max_length=100)
    image = models.ImageField(upload_to='work/%Y/%m', default='image/default.png', max_length=100, verbose_name='图片')
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


class UserAsk(models.Model):
    '''用户学习'''
    name = models.CharField('姓名',max_length=20)
    mobile = models.CharField('手机',max_length=11)
    course_name = models.CharField('课程名',max_length=50)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户学习'
        verbose_name_plural = '用户学习'

    def __str__(self):
        return self.name



