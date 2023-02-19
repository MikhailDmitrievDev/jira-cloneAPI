from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]