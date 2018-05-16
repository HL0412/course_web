"""course_web path Configuration

The `pathpatterns` list routes urls to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path('', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.urls import include, path
    2. Add a path to pathpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.static import serve
from course_web.settings import  MEDIA_ROOT
from django.urls import path, include, re_path

from users.views import IndexView, LoginView, LogoutView, RegisterView, ForgetPwdView, ModifyPwdView, ResetView, \
    ActiveUserView
from xadmin.plugins import xversion
import xadmin

#version模块自动注册需要版本控制的 Model
xversion.register_models()

xadmin.autodiscover()

urlpatterns = [

    # re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/',RegisterView.as_view(),name = 'register'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path('captcha/',include('captcha.urls')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 以下是创建的app的urls
    path('users/', include('users.urls', namespace='users')),
    path('college/', include('college.urls', namespace='college')),
    path('course/', include('course_manager.urls', namespace='course')),
    path('guestbook/', include('guestbook.urls', namespace='guestbook')),
    path('platfrom/', include('platfrom.urls', namespace='platfrom')),

    # 富文本相关url
    path('ueditor/',include('DjangoUeditor.urls' )),

]
# # 全局404页面配置
# handler404 = 'users.views.pag_not_found'
# # 全局500页面配置
# handler500 = 'users.views.page_error'