# Generated by Django 2.0.1 on 2018-02-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0009_auto_20180217_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='project',
        ),
        migrations.AddField(
            model_name='tasktags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Tag'),
        ),
        migrations.AddField(
            model_name='tasktags',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(through='taskmanager.TaskTags', to='taskmanager.Tag'),
        ),
    ]
