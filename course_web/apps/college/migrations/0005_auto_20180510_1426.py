# Generated by Django 2.0.2 on 2018-05-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_auto_20180510_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(max_length=50, verbose_name='班级名称'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('djx', '电子信息与计算机工程系'), ('tmx', '资源勘查与土木工程系'), ('zdh', '自动化工程系'), ('wyx', '外语系'), ('glx', '管理系'), ('ysx', '艺术设计系'), ('hnx', '核工程与新能源技术系'), ('jjx', '经济系')], default='djx', max_length=100, verbose_name='教学单位'),
        ),
    ]
