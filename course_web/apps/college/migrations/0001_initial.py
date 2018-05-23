# Generated by Django 2.0.4 on 2018-05-23 22:22

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='班级名称')),
                ('desc', DjangoUeditor.models.UEditorField(default='', verbose_name='班级描述')),
                ('image', models.ImageField(blank=True, default='image/default.png', null=True, upload_to='classroom/%Y/%m', verbose_name='班级图片')),
                ('grade', models.CharField(choices=[('freshman', '大一'), ('sophomore', '大二'), ('junior', '大三'), ('senior', '大四')], default='freshman', max_length=45, verbose_name='年级')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '班级信息',
                'verbose_name_plural': '班级信息',
                'db_table': 'classroom_info',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('djx', '电子信息与计算机工程系'), ('tmx', '资源勘查与土木工程系'), ('zdh', '自动化工程系'), ('wyx', '外语系'), ('glx', '管理系'), ('ysx', '艺术设计系'), ('hnx', '核工程与新能源技术系'), ('jjx', '经济系')], default='djx', max_length=100, verbose_name='教学单位')),
                ('desc', DjangoUeditor.models.UEditorField(default='', verbose_name='教学单位描述')),
                ('image', models.ImageField(blank=True, default='image/default.png', null=True, upload_to='department/%Y/%m', verbose_name='教学单位图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '教学单位',
                'verbose_name_plural': '教学单位',
                'db_table': 'department_info',
            },
        ),
        migrations.AddField(
            model_name='classroom',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.Department', verbose_name='所在教学单位'),
        ),
    ]
