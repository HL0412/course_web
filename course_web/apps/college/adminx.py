from django.contrib import admin

# Register your models here.
import xadmin
from college.models import Classroom, Department, Teacher, Student


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

class TeacherAdmin:
    list_display = ['teacher_name', 'teacher_num', 'teacher_rank', 'sex', 'age', 'department', 'phone', 'email', 'picture', 'add_time']
    search_fileds = ['teacher_name', 'teacher_num', 'teacher_rank', 'phone', 'email']
    list_filter = ['teacher_name', 'teacher_num', 'department', 'phone', 'teacher_rank', 'email']
    model_icon = 'fa fa-users'

class StudentAdmin:
    list_display = ['student_name', 'student_num', 'classroom', 'sex', 'age', 'phone', 'email', 'picture', 'add_time']
    search_fileds = ['student_name', 'student_num', 'phone', 'email']
    list_filter = ['student_name', 'student_num', 'classroom', 'phone', 'email']
    model_icon = 'fa fa-user-md'

xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(Department, DepartmentAdmin)
xadmin.site.register(Classroom, ClassroomAdmin)
