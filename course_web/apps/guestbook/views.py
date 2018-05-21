from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from pure_pagination import Paginator, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
# Create your views here.
from guestbook.forms import publishGuestbookForm
from guestbook.models import GuestBook


class GuestbookView(View):
    def get(self, request):
        all_guestbook = GuestBook.objects.all()
        hot_guestbook = GuestBook.objects.all().order_by('g_time')[:10]
        # 进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_guestbook, 10, request=request)
        all_guestbook = p.page(page)
        return render(request, 'guestbook/guestbook.html', {'all_guestbook': all_guestbook, 'hot_guestbook': hot_guestbook})


class PublishGuestbookView(LoginRequiredMixin,View):
    '''留言发布'''

    def post(self, request):
        if not request.user.is_authenticated:
            # 未登录时返回json提示未登录，跳转到登录页面是在ajax中做的
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        guestBook = GuestBook()
        if request.method == 'POST':
            publishGuestbookform = publishGuestbookForm(request.POST)
            if publishGuestbookform:
                title = request.POST.get('title')
                content = request.POST.get('content')
                date = request.POST.get('date')
                if title and content and date:
                    guestBook.user = request.user
                    guestBook.nickname =request.user.nick_name
                    guestBook.title = title
                    guestBook.g_content = content
                    guestBook.g_time = date
                    guestBook.save()
                    return HttpResponse('{"status":"success", "msg":"留言发表成功"}', content_type='application/json')
                else:
                    return HttpResponse('{"status":"fail", "msg":"留言发表失败"}', content_type='application/json')


class GuestbookDetailView(View):
    pass


class GuestbookSearchView(View):
    def get(self, request):
        q = request.GET.get('q')
        print(q)
        if q:
            guestbook_list = GuestBook.objects.filter(Q(title__icontains=q) | Q(g_content__icontains=q))
            return render(request, 'guestbook/guestbook.html', {'guestbook_list': guestbook_list})

