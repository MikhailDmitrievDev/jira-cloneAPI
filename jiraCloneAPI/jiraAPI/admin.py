from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectType)
admin.site.register(Categories)
admin.site.register(Task)
