# Generated by Django 2.0.1 on 2018-02-17 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0006_auto_20180217_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='harddeadline',
            field=models.DateField(default=datetime.date.today, help_text='Enter the hard deadline', verbose_name='Hard deadline'),
        ),
        migrations.AlterField(
            model_name='project',
            name='softdeadline',
            field=models.DateField(default=datetime.date.today, help_text='Enter the soft deadline', verbose_name='Soft deadline'),
        ),
    ]
