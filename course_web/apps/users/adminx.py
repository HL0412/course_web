from django.contrib import admin

# Register your models here.
from  xadmin import views
import xadmin
from users.models import Student, EmailVerifyRecord


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将基本配置管理与view绑定

# 全局修改，固定写法
class GlobalSettings(object):
    # 修改title
    site_title = '课程教学网站后台管理界面'
    # 修改footer
    site_footer = 'Huangli--成都理工大学工程技术学院'
    # # 收起菜单
    # menu_style = 'accordion'

class StudentAdmin:
    list_display = ['student_name', 'student_num', 'classroom', 'sex', 'age', 'phone', 'email', 'picture', 'add_time']
    search_fileds = ['student_name', 'student_num', 'phone', 'email']
    list_filter = ['student_name', 'student_num', 'classroom', 'phone', 'email']
    model_icon = 'fa fa-user-md'

class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']
    model_icon = 'fa fa-envelope'


xadmin.site.register(Student, StudentAdmin)
# xadmin.site.register(Users, UsersAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
# 将title和footer信息进行注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
