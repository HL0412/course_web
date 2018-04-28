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
    list_display = ['department', 'grade', 'major', 'classes', 'add_time']
    search_fileds = ['department', 'grade', 'major', 'classes']
    list_filter = ['department', 'grade', 'major', 'classes']
    model_icon = 'fa fa-info'

class TeacherAdmin:
    list_display = ['department', 'name', 'number', 'teacher_rank', 'sex', 'age',  'phone', 'email', 'image', 'add_time']
    search_fileds = ['name', 'number', 'rank', 'phone', 'email']
    list_filter = ['name', 'number', 'department', 'phone', 'teacher_rank', 'email']
    model_icon = 'fa fa-users'

class StudentAdmin:
    list_display = ['name', 'number', 'classroom', 'sex', 'age', 'phone', 'email', 'image', 'add_time']
    search_fileds = ['name', 'number', 'phone', 'email']
    list_filter = ['name', 'number', 'classroom', 'phone', 'email']
    model_icon = 'fa fa-user-md'

xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Classroom, ClassroomAdmin)
