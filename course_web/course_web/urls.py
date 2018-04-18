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
from django.urls import path, include, re_path
from users.views import IndexView, LoginView, LogoutView, RegisterView, ForgetPwdView, ModifyPwdView, ResetView, \
    ActiveUserView
from xadmin.plugins import xversion
import xadmin

#version模块自动注册需要版本控制的 Model
xversion.register_models()

xadmin.autodiscover()

urlpatterns = [

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

    # 以下是创建的app的urls
    path('users/', include('users.urls', namespace='users')),
    # path('college/', include('college.urls', namespace='college')),
    # path('course_manage/', include('course_manager.urls', namespace='course_manager')),
    # path('guestbook/', include('guestbook.urls', namespace='guestbook')),
    # path('platfrom/', include('platfrom.urls', namespace='platfrom')),


    # path('', TemplateView.as_view(template_name='index.html'),name='index'),
    # # path('login/', TemplateView.as_view(template_name='login.html'),name='login'),
    # path('login/', views.user_login, name='login'),  # 修改login路由


]
