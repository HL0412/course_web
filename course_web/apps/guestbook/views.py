from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import PageNotAnInteger, Paginator
from django.db.models import Q
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
# Create your views here.
from course_manager.models import Course


class GuestbookView(View):
    def get(self, request):
        return render(request, 'guestbook/guestbook.html')

class PublishGuestbookView(LoginRequiredMixin,View):
    def post(self, request):
        if not request.user.is_authenticated:
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"success"}', content_type='application/json')



