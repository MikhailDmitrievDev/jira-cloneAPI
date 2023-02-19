from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):

    projectName = models.CharField(max_length=100)
    projectKey = models.CharField(max_length=100, unique=True, null=True)
    dateCreateProject = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.projectName

class Task(models.Model):

    task_title = models.CharField(verbose_name='Название задачи', db_index=True,
                                  unique=True, max_length=100, blank=True)
    task_description = models.CharField(verbose_name='Описание задачи', max_length=150,
                                        blank=True)
    task_executor = models.ForeignKey(User, verbose_name='Исполнитель', on_delete=models.CASCADE)
    task_creator = models.CharField(verbose_name='Создал задачу', max_length=100)
    task_files = models.FileField(upload_to='task_files/', blank=False, null=True)
    task_comment = models.CharField(verbose_name='Комментарий', max_length=255, blank=True)
    task_date_create = models.DateTimeField(verbose_name='Дата создания задачи', auto_now_add=True)
    task_date_update = models.DateTimeField(auto_now=True)
    task_grade = models.CharField(max_length=150, null=False)
    task_remaning_time = models.IntegerField(verbose_name='Осталось времени на задачу', blank=True)
    task_spent_time = models.IntegerField(verbose_name='Потрачено времени на задачу', null=False)
    sprint_status = models.CharField(verbose_name='Статус спринта', max_length=150)
    task_apic = models.CharField(max_length=150, null=False)

    """
        TODO:
        Role users
    """
    def __str__(self):
        return self.task_title
class Dashboard(models.Model):
    dashboard_title = models.CharField(verbose_name='Название Доски', max_length=150)
    # dashBoardStatus
    dashboard_task_name = models.ForeignKey(Task, on_delete=models.CASCADE)
    def __str__(self):
        return self.dashboard_title

