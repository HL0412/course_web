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
from django.urls import path, include
from django.views.generic import TemplateView

from users import views
from xadmin.plugins import xversion
import xadmin

#version模块自动注册需要版本控制的 Model
xversion.register_models()

xadmin.autodiscover()

urlpatterns = [

    path('xadmin/', xadmin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('captcha/',include('captcha.urls')),
    # path('college/', include('college.urls', namespace='college')),
    # path('course_manage/', include('course_manager.urls', namespace='course_manager')),
    # path('guestbook/', include('guestbook.urls', namespace='guestbook')),
    # path('platfrom/', include('platfrom.urls', namespace='platfrom')),


    # path('', TemplateView.as_view(template_name='index.html'),name='index'),
    # # path('login/', TemplateView.as_view(template_name='login.html'),name='login'),
    # path('login/', views.user_login, name='login'),  # 修改login路由


]
