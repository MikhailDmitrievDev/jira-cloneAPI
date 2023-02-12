from django.db import models
from django.contrib.auth.models import User



class Categories(models.Model):

    categoriesName = models.CharField(max_length=150)
    categoriesDescription = models.CharField(max_length=255)
    def __str__(self):
        return self.categoriesName
class Methodology(models.Model):
    methodologyName = models.CharField(max_length=150)
    methodologyDescription = models.CharField(max_length=255)
    def __str__(self):
        return self.methodologyName
class ProjectType(models.Model):
    projectTypeName = models.CharField(max_length=150)
    projectTypeDescription = models.CharField(max_length=255)

    def __str__(self):
        return self.projectTypeName
class Project(models.Model):

    projectName = models.CharField(max_length=100)
    projectKey = models.CharField(max_length=100, unique=True, null=True)
    projectTypeID = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    dateCreateProject = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.projectName

class Task(models.Model):
    taskTitle = models.CharField(max_length=200)
    taskDescription = models.CharField(max_length=255)
    dateCreateProject = models.DateTimeField(auto_now_add=True)
    taskCreator = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    taskExecuter = models.CharField(max_length=100)
    def __str__(self):
        return self.taskTitle
class Dashboard(models.Model):
    dashboardTitle = models.CharField(max_length=150)
    dashboardTaskName = models.ForeignKey(Task, on_delete=models.CASCADE)
    def __str__(self):
        return self.dashboardTitle
class RoadMap(models.Model):
    epicTitle = models.CharField(max_length=120)
    def __str__(self):
        return self.epicTitle