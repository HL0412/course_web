# Generated by Django 2.0.2 on 2018-05-10 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_remove_classroom_course'),
        ('course_manager', '0004_course_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='college.Department', verbose_name='所属教学单位'),
            preserve_default=False,
        ),
    ]
