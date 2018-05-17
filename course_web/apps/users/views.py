# users/views.py
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.backends import ModelBackend
from django.urls import reverse
from pure_pagination import Paginator

from course_manager.models import Course
from platfrom.models import Notice, News, WorkCommit, UserMessage, UserCourse
from .models import UserProfile,EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm, UserInfoForm, UploadImageForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_eamil


#邮箱和用户名都可以登录
# 基与ModelBackend类，因为它有authenticate方法
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))

            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    '''首页'''
    def get(self, request):
        '''获取数据库中前四个课程信息'''
        course_one = Course.objects.get(id='1')
        course_two = Course.objects.get(id='2')
        course_three = Course.objects.get(id='3')
        course_four = Course.objects.get(id='4')
        notices = Notice.objects.all().order_by('-publish_time')[:10]
        news = News.objects.all().order_by('-publish_time')[:10]
        works = WorkCommit.objects.all()[:10]
        return render(request, "index.html", {'course_one' : course_one, 'course_two' : course_two, 'course_three' : course_three,
                                              'course_four' : course_four, 'notices' : notices, 'news' : news, 'works' : works})


class LoginView(View):
    '''用户登录'''

    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        # 实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取用户提交的用户名和密码
            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)
            rank = request.POST.get('rank', None)
            if rank == '学生':
                is_student = True
                is_teacher = False
            else:
                is_student = False
                is_teacher = True
            # 成功返回user对象,失败None
            user = authenticate(username=user_name, password=pass_word)

            # 如果不是null说明验证成功
            if user is not None:
                if user.is_student == is_student and user.is_teacher == is_teacher:
                    pass
                else:
                    return render(request, 'login.html', {'msg': '用户权限不对', 'login_form': login_form})

                if user.is_active:
                    # 只有注册激活才能登录
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', {'msg': '请前往邮箱激活账号', 'login_form': login_form})
            # 只有当用户名或密码不存在时，才返回错误信息到前端
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误','login_form':login_form})


        else:
            return render(request,'login.html',{'login_form':login_form})

# 激活用户
class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code = active_code)

        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 查找到邮箱对应的user
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
         # 验证码不对的时候跳转到激活失败页面
        else:
            return render(request,'active_fail.html')
        # 激活成功跳转到登录页面
        return render(request, "login.html", )


class LogoutView(View):
    '''用户退出'''
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


# 注册
class RegisterView(View):
    '''用户注册'''
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        # 实例化一个user_profile对象
        user_profile = UserProfile()
        if register_form.is_valid():
            username = request.POST.get('username', None)
            user_name = request.POST.get('email', None)
            # 如果用户已存在，则提示错误信息
            if UserProfile.objects.filter(email = username):
                return render(request, 'register.html', {'register_form':register_form,'msg': '用户已存在'})
            pass_word = request.POST.get('password', None)
            check_box_list = request.POST.get('check_box_list', None)

            if int(check_box_list) == 1:
                user_profile.is_student = 1
            else:
                user_profile.is_teacher = 1

            user_profile.username = username
            user_profile.email = user_name
            user_profile.is_active = False
            # 对保存到数据库的密码加密
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_eamil(user_name,'register')
            return render(request,'login.html')
        else:
            return render(request,'register.html',{'register_form':register_form})


class ForgetPwdView(View):
    '''找回密码'''
    def get(self,request):
        forget_form = ForgetPwdForm()
        return render(request,'forgetpwd.html',{'forget_form':forget_form})

    def post(self,request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email',None)
            send_register_eamil(email,'forget')
            return render(request, 'send_success.html')
        else:
            return render(request,'forgetpwd.html',{'forget_form':forget_form})


class ResetView(View):
    '''重置密码'''
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email":email})
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")

class ModifyPwdView(View):
    '''修改用户密码'''
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email":email, "msg":"密码不一致！"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email":email, "modify_form":modify_form })



class UserinfoView(LoginRequiredMixin, View):
    '''用户个人信息'''
    def get(self,request):
        current_page = 'myself'
        return render(request,'users/usercenter_info.html', {"current_page" : current_page})

    def post(self, request):

        print(request.user)
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        print(user_info_form.is_valid())
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class UploadImageView(LoginRequiredMixin,View):
    '''用户图像修改'''
    def post(self,request):
        #上传的文件都在request.FILES里面获取，所以这里要多传一个这个参数
        image_form = UploadImageForm(request.POST,request.FILES)
        if image_form.is_valid():
            image = image_form.cleaned_data['image']
            request.user.image = image
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class UpdatePwdView(LoginRequiredMixin,View):
    """
    个人中心修改用户密码
    """
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return HttpResponse('{"status":"fail","msg":"密码不一致"}',  content_type='application/json')
            user = request.user
            user.password = make_password(pwd2)
            user.save()

            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')


class SendEmailCodeView(LoginRequiredMixin, View):
    '''发送邮箱修改验证码'''
    def get(self,request):
        email = request.GET.get('email','')

        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已存在"}', content_type='application/json')

        send_register_eamil(email,'update_email')
        return HttpResponse('{"status":"success"}', content_type='application/json')



class UpdateEmailView(LoginRequiredMixin, View):
    '''修改邮箱'''
    def post(self, request):
        email = request.POST.get("email", "")
        code = request.POST.get("code", "")

        existed_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='update_email')
        if existed_records:
            user = request.user
            user.email = email
            user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"email":"验证码无效"}', content_type='application/json')


class MyCourseView(LoginRequiredMixin, View):
    '''我的课程--学生'''
    def get(self, request):
        current_page = 'mycourse'
        user_courses = UserCourse.objects.filter(user=request.user)
        print(user_courses)
        return render(request, "users/usercenter_mycourse.html", {
            "user_courses" : user_courses,
            "current_page" : current_page
        })

class MyTeachCourseView(LoginRequiredMixin, View):
    '''我所教的课程--教师'''
    def get(self, request):
        current_page = 'my_teach_course'
        user_courses = UserCourse.objects.filter(user=request.user)
        print(user_courses)
        return render(request, "users/usercenter_my_teach_course.html", {
            "user_courses" : user_courses,
            "current_page" : current_page
        })


class MyWorkView(LoginRequiredMixin,View):
    '''我的作业'''

    def get(self, request):
        current_page = 'mywork'
        return render(request, "users/usercenter_work.html" ,{'current_page': current_page})

class MyPublishWorkView(LoginRequiredMixin,View):
    '''我发布作业'''

    def get(self, request):
        current_page = 'my_publish_work'
        return render(request, "users/usercenter_publish_work.html" ,{'current_page': current_page})


class WorkFinishView(LoginRequiredMixin,View):
    '''我提交的作业'''
    def get(self, request):
        return render(request, "users/usercenter_workfinish.html")


class MyMessageView(LoginRequiredMixin, View):
    '''我的消息'''

    def get(self, request):
        current_page = 'mymessage'
        all_message = UserMessage.objects.filter(user=request.user.id)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_message, 10, request=request)
        messages = p.page(page)
        return  render(request, "users/usercenter_message.html", {
            "messages":messages,
            'current_page': current_page
        })


from django.shortcuts import render_to_response
def pag_not_found(request):
    # 全局404处理函数
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

def page_error(request):
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response