from django.contrib import admin
from todo_app.models import TaskList, Category

# Register your models here.
admin.site.register(TaskList)
admin.site.register(Category)