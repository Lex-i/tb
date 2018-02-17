# Generated by Django 2.0.1 on 2018-02-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='harddeadline',
            field=models.DateField(auto_now=True, help_text='Enter the hard deadline', verbose_name='Hard deadline'),
        ),
        migrations.AddField(
            model_name='project',
            name='softdeadline',
            field=models.DateField(auto_now=True, help_text='Enter the soft deadline', verbose_name='Soft deadline'),
        ),
    ]
