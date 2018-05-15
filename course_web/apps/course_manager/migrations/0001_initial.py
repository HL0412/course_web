# Generated by Django 2.0.2 on 2018-05-15 10:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='课程名')),
                ('course_num', models.IntegerField(unique=True, verbose_name='课程号')),
                ('course_intro', models.TextField(blank=True, null=True, verbose_name='课程介绍')),
                ('image', models.ImageField(blank=True, default='image/default.png', null=True, upload_to='classroom/%Y/%m', verbose_name='班级图片')),
                ('course_picture', models.ImageField(blank=True, default='image/default.png', null=True, upload_to='course/image/%Y/%m', verbose_name='课程图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
                'db_table': 'course_info',
            },
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_name', models.CharField(max_length=100, verbose_name='资料名称')),
                ('data', models.FileField(upload_to='course/data/%Y/%m', verbose_name='课程资料')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课程资料',
                'verbose_name_plural': '课程资料',
                'db_table': 'course_data',
            },
        ),
        migrations.CreateModel(
            name='PPT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppt_name', models.CharField(max_length=100, verbose_name='课件名称')),
                ('ppt', models.FileField(upload_to='course/ppt/%Y/%m', verbose_name='课件')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '课件',
                'verbose_name_plural': '课件',
                'db_table': 'course_ppt',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='姓名')),
                ('number', models.CharField(max_length=45, unique=True, verbose_name='学号')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
                'db_table': 'student_info',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='姓名')),
                ('number', models.CharField(max_length=45, verbose_name='职工号')),
                ('work_years', models.CharField(max_length=45, verbose_name='教学年限')),
                ('rank', models.CharField(max_length=45, verbose_name='职称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Classroom', verbose_name='所属班级')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Department', verbose_name='所属教学单位')),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
                'db_table': 'teacher_info',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=100, verbose_name='视频名')),
                ('url', models.URLField(max_length=150, verbose_name='视频地址')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习时长（分钟数)')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_manager.Course', verbose_name='课程名')),
            ],
            options={
                'verbose_name': '课程视频',
                'verbose_name_plural': '课程视频',
                'db_table': 'course_video',
            },
        ),
    ]
