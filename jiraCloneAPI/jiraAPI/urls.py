from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('task/', TaskViewSet.as_view({'get': 'list'})),
    path('task/create/', TaskViewSet.as_view({'post': 'create'})),
    path('task/<int:pk>/', TaskViewSet.as_view({
        'put': 'update',
        'get': 'list',
        'delete': 'destroy'
    }))
]