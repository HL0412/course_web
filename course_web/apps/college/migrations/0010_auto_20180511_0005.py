# Generated by Django 2.0.4 on 2018-05-11 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_auto_20180510_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='image',
            field=models.ImageField(blank=True, default='image/default.png', null=True, upload_to='classroom/%Y/%m', verbose_name='班级图片'),
        ),
    ]
