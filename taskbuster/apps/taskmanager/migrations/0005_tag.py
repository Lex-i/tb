# Generated by Django 2.0.1 on 2018-02-16 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0004_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tags', to='taskmanager.Employee', verbose_name='user')),
            ],
            options={
                'ordering': ('user', 'name'),
                'verbose_name_plural': 'Tags',
                'verbose_name': 'Tag',
            },
        ),
    ]