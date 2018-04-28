# Generated by Django 2.0.2 on 2018-04-28 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=45, null=True, verbose_name='留言者')),
                ('title', models.CharField(max_length=45, verbose_name='标题')),
                ('g_content', models.TextField(verbose_name='内容')),
                ('g_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='留言时间')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别')),
                ('ID_Card', models.CharField(default=0, max_length=50, verbose_name='留言ID')),
                ('checkout', models.BooleanField(default=False, verbose_name='是否通过审核')),
                ('r_content', models.TextField(verbose_name='回复内容')),
                ('r_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='回复时间')),
                ('type', models.IntegerField(choices=[(1, '发表'), (2, '回复')], default=1, verbose_name='类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'db_table': 'guestbook_info',
                'verbose_name': '留言管理',
                'verbose_name_plural': '留言管理',
            },
        ),
    ]
