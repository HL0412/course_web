# Generated by Django 2.0.2 on 2018-05-10 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_auto_20180510_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='course',
        ),
    ]
