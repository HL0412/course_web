from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from platfrom.models import Notice, WorkCommit, News


class NoticeListView(View):
    def get(self, request):
        all_notices = Notice.objects.all().order_by('-publish_time')
        return render(request, 'platfrom/notice_list.html', {'notices' : all_notices})


class NoticeDetailView(View):
    def get(self, request):
        notice_id = request.GET.get('notice_id')
        notice = Notice.objects.filter(notice_id)
        return render(request, 'platfrom/notice_detail.html', {'notice' : notice})


class NewsListView(View):
    def get(self, request):
        all_news = News.objects.all().order_by('-publish_time')
        return render(request, 'platfrom/news_list.html', {'news': all_news})


class NewsDetailView(View):
    def get(self, request):
        news_id = request.GET.get('news_id')
        news = News.objects.get(news_id)
        return render(request, 'platfrom/news_detail.html', {'news': news})


class WorkListView(View):
    def get(self, request):
        all_work = WorkCommit.objects.all()
        return render(request, 'platfrom/work_list.html', {'work': all_work})


class PlatfromListView(View):
    def get(self, request):
        return render(request, 'platfrom/platfrom_list.html')