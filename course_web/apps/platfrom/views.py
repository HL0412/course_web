from pure_pagination import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from college.models import Classroom
from platfrom.models import Notice, WorkCommit, News


class NoticeListView(View):
    def get(self, request):
        all_notices = Notice.objects.all().order_by('-publish_time')
        return render(request, 'platfrom/notice_list.html', {'notices' : all_notices})


class NoticeDetailView(View):
    def get(self, request, notice_id):
        notice = Notice.objects.get(id=int(notice_id))
        return render(request, 'platfrom/notice_detail.html', {'notice' : notice})


class NewsListView(View):
    def get(self, request):
        all_news = News.objects.all().order_by('-publish_time')
        return render(request, 'platfrom/news_list.html', {'news': all_news})


class NewsDetailView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=int(news_id))
        return render(request, 'platfrom/news_detail.html', {'news': news})


class WorkListView(View):

    def get(self, request):

        all_work = WorkCommit.objects.all().order_by('-commit_time')
        grade = request.GET.get('grade', "")
        if grade:
            if grade == 'freshman':
                all_work = all_work.filter(grade=grade)
            elif grade == 'sophomore':
                all_work = all_work.filter(grade=grade)
            elif grade == 'junior':
                all_work = all_work.filter(grade=grade)
            elif grade == 'senior':
                all_work = all_work.filter(grade=grade)
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_work, 10, request=request)
        works = p.page(page)
        return render(request, 'platfrom/work_list.html', {
            'works': works,
            'grade': grade,
        })


class WorkDetailView(View):
    def get(self, request, work_id):
        work = WorkCommit.objects.get(id=int(work_id))
        return render(request, 'platfrom/work_detail.html', {'work': work})

class CommitWorktView(View):
    def get(self, request):
        current_page = "commitWork"
        return render(request, 'platfrom/platfrom_commitWork.html',{'current_page':current_page})

class DownPPTView(View):
    def get(self, request):
        current_page = "down_ppt"
        return render(request, 'platfrom/platfrom_commitWork.html',{'current_page':current_page})

class DownDataView(View):
    def get(self, request):
        current_page = "down_data"
        return render(request, 'platfrom/platfrom_commitWork.html',{'current_page':current_page})

class PublishWorkView(View):
    def get(self, request):
        current_page = "publishWork"
        return render(request, 'platfrom/platfrom_commitWork.html',{'current_page':current_page})

class UpPPTView(View):
    def get(self, request):
        current_page = "up_ppt"
        return render(request, 'platfrom/platfrom_commitWork.html',{'current_page':current_page})

class UpDataView(View):
    def get(self, request):
        current_page = "up_data"
        return render(request, 'platfrom/platfrom_commitWork.html',{'current_page':current_page})

class UpVideoView(View):
    def get(self, request):
        current_page = "up_video"
        return render(request, 'platfrom/platfrom_commitWork.html',{'current_page':current_page})
