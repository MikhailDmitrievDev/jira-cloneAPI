# Generated by Django 4.1.6 on 2023-02-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiraAPI', '0026_rename_sprint_status_task_sprint_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_title',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Название задачи'),
        ),
    ]