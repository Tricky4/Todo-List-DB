from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo_app.api.views import (TaskDetailAV, CategoryList, TaskListAV, TaskListGV)

router = DefaultRouter()
router.register('category', CategoryList, basename='categorylist')

urlpatterns = [
    path('<int:pk>/', TaskDetailAV.as_view(), name='task-detail'),
    path('list/', TaskListAV.as_view(), name='task-list'),
    path('list-page/', TaskListGV.as_view(), name='task-page'),
    path('', include(router.urls)),
]