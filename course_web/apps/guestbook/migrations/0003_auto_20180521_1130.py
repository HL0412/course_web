# Generated by Django 2.0.2 on 2018-05-21 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0002_guestbook_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestbook',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='guestbook',
            name='ID_Card',
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='r_content',
            field=models.TextField(blank=True, null=True, verbose_name='回复内容'),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='r_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='回复时间'),
        ),
    ]
