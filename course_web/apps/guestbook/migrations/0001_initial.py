# Generated by Django 2.0.2 on 2018-05-25 13:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='标题')),
                ('g_content', models.TextField(verbose_name='内容')),
                ('g_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='留言时间')),
            ],
            options={
                'db_table': 'guestbook_info',
                'verbose_name': '留言管理',
                'verbose_name_plural': '留言管理',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_content', models.TextField(verbose_name='回复内容')),
                ('r_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='回复时间')),
                ('guestbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guestbook.GuestBook', verbose_name='留言')),
                ('parent_reply', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='guestbook.Reply')),
            ],
            options={
                'db_table': 'reply_info',
                'verbose_name': '留言回复管理',
                'verbose_name_plural': '留言回复管理',
            },
        ),
    ]
