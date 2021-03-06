# Generated by Django 2.0.1 on 2018-05-07 19:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, help_text='Enter description', null=True, verbose_name='Description')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date & time')),
            ],
            options={
                'ordering': ('datetime',),
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=1, help_text='Enter the Department name', max_length=100, verbose_name='Department name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the employee's name", max_length=100, verbose_name='Full name')),
                ('int_phone', models.PositiveIntegerField(default=100, help_text='Enter the internal phone number', verbose_name='Internal phone')),
                ('ext_phone', models.CharField(help_text='Enter the external (mobile) phone number', max_length=12, verbose_name='External phone')),
                ('job_title', models.CharField(help_text="Enter the employee's job title", max_length=100, verbose_name='Job title')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_staff', to='taskmanager.Department', verbose_name='Department')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinate_employees', to='taskmanager.Employee', verbose_name='Supervisor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the project name', max_length=120, verbose_name='Project Title')),
                ('description', models.TextField(blank=True, help_text='Enter description', null=True, verbose_name='Description')),
                ('priority', models.PositiveSmallIntegerField(default=1, help_text='Enter the priority of the project', verbose_name='Priority')),
                ('softdeadline', models.DateField(default=datetime.date.today, help_text='Enter the soft deadline', verbose_name='Soft deadline')),
                ('harddeadline', models.DateField(default=datetime.date.today, help_text='Enter the hard deadline', verbose_name='Hard deadline')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='taskmanager.Employee', verbose_name='Project Manager')),
            ],
            options={
                'ordering': ('priority', 'name'),
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avail_projects', to='taskmanager.Employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_team', to='taskmanager.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tag Name')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags', to='taskmanager.Employee', verbose_name='user')),
            ],
            options={
                'ordering': ('user', 'name'),
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the task title', max_length=120, verbose_name='Task Title')),
                ('completed', models.BooleanField(default=False, verbose_name='completed')),
                ('priority', models.PositiveSmallIntegerField(default=1, help_text='Enter the priority of the task', verbose_name='Priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created date')),
                ('due_date', models.DateField(default=datetime.date.today, help_text='Enter the planned due date', verbose_name='Due date')),
                ('completed_date', models.DateField(blank=True, null=True, verbose_name='Completed date')),
                ('description', models.TextField(blank=True, help_text='Enter description', null=True, verbose_name='Description')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to='taskmanager.Employee', verbose_name='Task assignee')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_tasks', to='taskmanager.Employee', verbose_name='Task Owner')),
                ('parenttask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtasks', to='taskmanager.Task', verbose_name='Parent task')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_tasks', to='taskmanager.Project', verbose_name='project')),
            ],
            options={
                'ordering': ('priority', 'name'),
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='TaskTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Tag')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskmanager.Task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(through='taskmanager.TaskTags', to='taskmanager.Tag'),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(through='taskmanager.ProjectTeam', to='taskmanager.Employee'),
        ),
        migrations.AddField(
            model_name='department',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_department', to='taskmanager.Employee', verbose_name='Supervisor'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_comments', to='taskmanager.Employee', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_comments', to='taskmanager.Project', verbose_name='Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='taskmanager.Comment', verbose_name='In reply to'),
        ),
    ]
