# Generated by Django 4.1.6 on 2023-02-19 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jiraAPI', '0025_rename_task_comment_task_task_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='sprint_Status',
            new_name='sprint_status',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_Apic',
            new_name='task_apic',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_Remaning_time',
            new_name='task_remaning_time',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_Spent_time',
            new_name='task_spent_time',
        ),
    ]
