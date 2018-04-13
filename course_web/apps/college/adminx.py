from django.contrib import admin

# Register your models here.
import xadmin
from college.models import Classroom, Department

class DepartmentAdmin:
    list_display = ['department_name', 'number', 'add_time']
    search_fileds = ['department_name', 'number']
    list_filter = ['department_name', 'number']
    model_icon = 'fa fa-home'

class ClassroomAdmin:
    list_display = ['department', 'grade', 'major', 'classes', 'add_time']
    search_fileds = ['department', 'grade', 'major', 'classes']
    list_filter = ['department', 'grade', 'major', 'classes']
    model_icon = 'fa fa-info'

xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Classroom, ClassroomAdmin)
