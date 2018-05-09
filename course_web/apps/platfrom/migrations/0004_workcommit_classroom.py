# Generated by Django 2.0.2 on 2018-05-09 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20180509_1332'),
        ('platfrom', '0003_workcommit_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='workcommit',
            name='classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='college.Classroom', verbose_name='班级'),
            preserve_default=False,
        ),
    ]