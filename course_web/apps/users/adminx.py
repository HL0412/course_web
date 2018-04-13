from django.contrib import admin

# Register your models here.
import xadmin
from users.models import Student, Teacher, Users

class UsersAdmin:
    list_display = ['name', 'username', 'password', 'categroy', 'add_time']
    search_fileds = ['username', 'password', 'categroy', 'name']
    list_filter =  ['username', 'password', 'categroy', 'name']
    model_icon = 'fa fa-user-md'

class StudentAdmin:
    list_display = ['student_name', 'student_num', 'classroom', 'sex', 'age', 'phone', 'email', 'picture', 'add_time']
    search_fileds = ['student_name', 'student_num', 'phone', 'email']
    list_filter = ['student_name', 'student_num', 'classroom', 'phone', 'email']
    model_icon = 'fa fa-user'

class TeacherAdmin:
    list_display = ['teacher_name', 'teacher_num', 'sex', 'age', 'department', 'phone', 'email', 'picture', 'add_time']
    search_fileds = ['teacher_name', 'teacher_num', 'phone', 'email']
    list_filter = ['teacher_name', 'teacher_num', 'department', 'phone', 'email']
    model_icon = 'fa fa-user'

xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Users, UsersAdmin)
