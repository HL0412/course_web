# Generated by Django 2.0.2 on 2018-05-04 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
        ('course_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_teacher',
        ),
        migrations.AddField(
            model_name='course',
            name='course_teacher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='college.Teacher', verbose_name='课程教师'),
            preserve_default=False,
        ),
    ]
