from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from xadmin.layout import *

from django.utils.translation import ugettext_lazy as _, ugettext

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'

xadmin.site.register(Log, LogAdmin)

from xadmin import views

# 添加标题和底部
class GlobalSetting:
    # 设置base_site.html的Title
    site_title = '课程教学网站后台管理'
    # 设置base_site.html的Footer
    site_footer = 'Huangli--成都理工大学工程技技术学院 '
    #设置菜单折叠
    menu_style = "accordion"
    # global_search_models = [V_UserInfo, UserDistrict]
    # global_models_icon = {
    #     V_UserInfo: "glyphicon glyphicon-user", UserDistrict: "fa fa-cloud"
    # }  # 设置models的全局图标
    # menu_style = "default"


xadmin.site.register(views.CommAdminView, GlobalSetting)