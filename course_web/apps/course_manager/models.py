from datetime import datetime
from django.db import models
# Create your models here.
from college.models import Classroom, Department
from users.models import UserProfile
class Teacher(models.Model):
    '''教师表'''
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True, verbose_name='用户名')
    classroom = models.ForeignKey(Classroom, verbose_name='所属班级', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name='所属教学单位', on_delete=models.CASCADE)
    name = models.CharField(max_length=45, verbose_name='姓名')
    number = models.CharField(max_length=45, verbose_name='职工号')
    work_years = models.CharField(max_length=45, verbose_name='教学年限')
    rank = models.CharField(max_length=45, verbose_name='职称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'teacher_info'
        verbose_name = '教师信息'
        verbose_name_plural = "教师信息"

    def get_course_nums(self):
        # 获取课程的教师数
        return self.course_set.all().count()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=45, verbose_name=u"课程名")
    course_num = models.IntegerField(unique=True, verbose_name=u"课程号")
    course_intro = models.TextField(null=True, blank=True, verbose_name='课程介绍')
    image = models.ImageField(null=True, blank=True, upload_to='classroom/%Y/%m', default='image/default.png',
                              max_length=100, verbose_name="班级图片")
    teacher = models.ForeignKey(Teacher, verbose_name='课程教师', on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, verbose_name='所属班级', on_delete=models.CASCADE)
    course_picture = models.ImageField(null=True, blank=True, upload_to='course/image/%Y/%m', default='image/default.png', max_length=100, verbose_name='课程图片')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    class Meta:
        db_table = 'course_info'
        verbose_name = '课程信息'
        verbose_name_plural = "课程信息"

    def get_student_nums(self):
        # 获取课程的学生数
        return self.student_set.all().count()

    def get_video(self):
        return self.video_set.all()

    def get_data(self):
        return self.data_set.all()

    def get_ppt(self):
        return self.ppt_set.all()

    def get_teacher(self):
        return self.teacher_set.all()

    def __str__(self):
        return self.name




class Student(models.Model):
    '''学生表'''
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True, verbose_name='用户名')
    classroom = models.ForeignKey(Classroom, verbose_name='所属班级', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='所学课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=45, verbose_name='姓名')
    number = models.CharField(max_length=45, unique=True, verbose_name='学号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'student_info'
        verbose_name = '学生信息'
        verbose_name_plural = "学生信息"

    def __str__(self):
        return self.name


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
    data = models.FileField(upload_to='course/data/%Y/%m', verbose_name='课程资料', max_length=100)
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
    ppt = models.FileField(upload_to='course/ppt/%Y/%m', verbose_name='课件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'course_ppt'
        verbose_name = '课件'
        verbose_name_plural = '课件'

    def __str__(self):
        return self.ppt_name

