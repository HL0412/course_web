from django.contrib import admin

# Register your models here.
import xadmin
from college.models import Classroom, Department, Teacher, Student


class DepartmentAdmin:
    list_display = ['name', 'desc', 'add_time']
    search_fileds = ['name']
    list_filter = ['name', 'add_time']
    model_icon = 'fa fa-home'

class ClassroomAdmin:
    list_display = ['name', 'department', 'grade', 'classes', 'add_time']
    search_fileds = ['name', 'department', 'grade',  'classes']
    list_filter = ['name', 'department', 'grade', 'classes']
    model_icon = 'fa fa-info'

class TeacherAdmin:
    list_display = ['name', 'number', 'rank',  'classroom', 'add_time']
    search_fileds = ['name', 'number']
    list_filter = ['name', 'number', 'classroom']
    model_icon = 'fa fa-users'

class StudentAdmin:
    list_display = ['name', 'number', 'classroom', 'add_time']
    search_fileds = ['name', 'number']
    list_filter = ['name', 'number', 'classroom']
    model_icon = 'fa fa-user-md'


xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Classroom, ClassroomAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(Student, StudentAdmin)
