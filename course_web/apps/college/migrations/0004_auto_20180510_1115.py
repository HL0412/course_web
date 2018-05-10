# Generated by Django 2.0.2 on 2018-05-10 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_manager', '0003_remove_course_course_teacher'),
        ('college', '0003_auto_20180509_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='major',
        ),
        migrations.AddField(
            model_name='classroom',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course_manager.Course', verbose_name='班级课程'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(max_length=50, verbose_name='专业名称'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('djx', '电子信息与计算机工程系'), ('tmx', '资源勘查与土木工程系'), ('zih', '自动化工程系'), ('wyx', '外语系'), ('glx', '管理系'), ('ysx', '艺术设计系'), ('hnx', '核工程与新能源技术系'), ('jjx', '经济系')], default='djx', max_length=100, verbose_name='教学单位'),
        ),
    ]
