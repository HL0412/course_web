from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.


class Department(models.Model):
    '''教学单位'''
    NAME_CHOICES = (

        ("djx", u"电子信息与计算机工程系"),
        ("tmx", u"资源勘查与土木工程系"),
        ("zdh", u"自动化工程系"),
        ("wyx", u"外语系"),
        ("glx", u"管理系"),
        ("ysx", u"艺术设计系"),
        ("hnx", u"核工程与新能源技术系"),
        ("jjx", u"经济系"),

    )
    name = models.CharField(max_length=100, choices=NAME_CHOICES, default='djx', verbose_name='教学单位')
    desc = UEditorField(verbose_name='教学单位描述', width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/", default='')
    image = models.ImageField(blank=True, null=True, upload_to='department/%Y/%m', default='image/default.png', max_length=100,
                              verbose_name="教学单位图片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        db_table = 'department_info'
        verbose_name = '教学单位'
        verbose_name_plural = '教学单位'

    def __str__(self):
        if self.name == 'djx':
            self.name = '电子信息与计算机工程系'
        if self.name == 'tmx':
            self.name = ' 资源勘查与土木工程系'
        if self.name == 'ysx':
            self.name = '艺术设计系'
        if self.name == 'wyx':
            self.name = '外语系'
        if self.name == 'hnx':
            self.name = '核工程与新能源技术系'
        if self.name == 'glx':
            self.name = '管理系'
        if self.name == 'jjx':
            self.name = '经济系'
        if self.name == 'zdh':
            self.name = '自动化工程系'

        return self.name



class Classroom(models.Model):
    '''班级'''
    GRADE_CHOICES = (

        ("freshman", u"大一"),
        ("sophomore", u"大二"),
        ("junior", u"大三"),
        ("senior", u"大四"),

    )
    name = models.CharField(max_length=50, verbose_name='班级名称')
    desc =  desc = UEditorField(verbose_name='班级描述', width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/", default='')
    department = models.ForeignKey(Department, verbose_name='所在教学单位', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='classroom/%Y/%m', default='image/default.png',
                      max_length=100, verbose_name = "班级图片")
    grade = models.CharField(max_length=45, choices=GRADE_CHOICES,verbose_name='年级', default="freshman")
    students = models.IntegerField(null=True, blank=True, verbose_name='学生人数')
    course_nums = models.IntegerField(null=True, blank=True,  verbose_name='课程数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        db_table = 'classroom_info'
        verbose_name = '班级信息'
        verbose_name_plural = "班级信息"

    def get_teacher_nums(self):
        #获取班级的教师数

        return self.teacher_set.all().count()

    def get_course_nums(self):
        # 获取班级的课程数
        return self.course_set.all().count()
    
    def get_student_nums(self):
        # 获取班级的学生数
        students = self.student_set.all().count()
        return students

    def __str__(self):
        return  self.name

