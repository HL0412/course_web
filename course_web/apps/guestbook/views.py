
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from pure_pagination import Paginator, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from guestbook import utils
from guestbook.forms import PublishGuestbookForm, ReplyForm
from guestbook.models import GuestBook, Reply

# Create your views here.
from utils.mixin_utils import LoginRequiredMixin


class GuestbookView(LoginRequiredMixin, View):
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
            publishGuestbookform = PublishGuestbookForm(request.POST)
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


class GuestbookSearchView(View):
    def get(self, request):
        hot_guestbook = GuestBook.objects.all().order_by('g_time')[:10]
        q = request.GET.get('q')
        if q:
            all_guestbook = GuestBook.objects.filter(Q(title__icontains=q) | Q(g_content__icontains=q))
            if not all_guestbook:
                return HttpResponse('{"status":"fail", "msg":"没有此关键字相关留言,请重新输入关键字！！！"}', content_type='application/json')
            else:
                # 进行分页
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(all_guestbook, 10, request=request)
                all_guestbook = p.page(page)
                return render(request, 'guestbook/guestbook.html', {'all_guestbook': all_guestbook, 'hot_guestbook':hot_guestbook})


class GuestbookDetailView(LoginRequiredMixin, View):
    def get(self, request, guestbook_id):
        guestbook_obj = GuestBook.objects.get(id=int(guestbook_id))
        reply_tree = utils.create_reply_tree(guestbook_obj)

        # 分页功能的实现
        # all_reply = [(k,) + tuple(v) for k, v in reply_tree.items()]
        # print(all_reply)
        #
        # try:
        #     page = request.GET.get('page', 1)
        # except PageNotAnInteger:
        #     page = 1
        # p = Paginator(all_reply, 1, request=request)
        # all_reply = p.page(page)
        # return render(request, 'guestbook/guestbook_detail.html', {'guestbook': guestbook_obj, 'reply_tree': reply_tree, 'all_reply':all_reply})
        return render(request, 'guestbook/guestbook_detail.html',
                      {'guestbook': guestbook_obj, 'reply_tree': reply_tree})

class ReplyView(LoginRequiredMixin, View):

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        reply =Reply()
        if request.method == 'POST':
            replyForm = ReplyForm(request.POST)
            if replyForm:
                content = request.POST.get('reply_content')
                date = request.POST.get('date')
                guestbook_id = request.POST.get('id')
                if content and date and id:
                    reply.user = request.user
                    reply.r_content = content
                    reply.r_time = date
                    reply.guestbook_id = guestbook_id
                    reply.save()
                    return HttpResponse('{"status":"success", "msg":"留言回复成功" }', content_type='application/json')
                else:
                    return HttpResponse('{"status":"fail", "msg":"留言回复失败"}', content_type='application/json')

class Reply_ReplyView(LoginRequiredMixin, View):

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        reply =Reply()
        if request.method == 'GET':
            id = request.GET.get('id')
            content = request.GET.get('reply_content')
            date = request.GET.get('date')
            reply_id = request.GET.get('reply_id')
            if content and date and reply_id:
                reply.user = request.user
                reply.r_content = content
                reply.r_time = date
                reply.parent_reply_id = reply_id
                reply.guestbook_id = id
                reply.save()
                return HttpResponse('{"status":"success", "msg":"留言回复成功" }', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"留言回复失败"}', content_type='application/json')